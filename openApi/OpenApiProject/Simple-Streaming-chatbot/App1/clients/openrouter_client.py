import json
import logging
from typing import Generator

import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

from App1.core.config import api_setting

logger = logging.getLogger(__name__)

HEADERS = {
    "Authorization": f"Bearer {api_setting.API_ROUTER_KEY}",
    "Content-Type": "application/json",
}


def _session() -> requests.Session:
    """
    Session with automatic retries on transient failures (connection errors,
    502/503/504). Prevents one flaky request from crashing the whole app.
    """
    session = requests.Session()
    retries = Retry(
        total=3,
        backoff_factor=0.5,
        status_forcelist=[502, 503, 504],
        allowed_methods=["POST"],
    )
    session.mount("https://", HTTPAdapter(max_retries=retries))
    return session


class OpenRouterError(Exception):
    """Raised when OpenRouter returns an error or an unreadable response."""


def chat_completion(messages: list[dict]) -> dict:
    """Non-streaming call — returns the full response in one shot."""
    try:
        response = _session().post(
            url=api_setting.OPENROUTER_URL,
            headers=HEADERS,
            json={
                "model": api_setting.OPENROUTER_MODEL,
                "messages": messages,
            },
            timeout=api_setting.REQUEST_TIMEOUT,
        )
        response.raise_for_status()
        return response.json()
    except requests.exceptions.Timeout as e:
        raise OpenRouterError("OpenRouter request timed out") from e
    except requests.exceptions.HTTPError as e:
        # Don't leak raw response bodies (may contain sensitive info) — log
        # full detail server-side, return a clean message to the caller.
        logger.error("OpenRouter HTTP error: %s | body=%s", e, response.text[:500])
        raise OpenRouterError(f"OpenRouter returned {response.status_code}") from e
    except requests.exceptions.RequestException as e:
        raise OpenRouterError("Failed to reach OpenRouter") from e


def chat_completion_stream(messages: list[dict]) -> Generator[str, None, None]:
    """
    Streaming call — yields text chunks as they arrive (SSE), instead of
    waiting for the whole answer. This is what actually gives you a
    "typing" effect in the terminal / UI.
    """
    try:
        with _session().post(
            url=api_setting.OPENROUTER_URL,
            headers=HEADERS,
            json={
                "model": api_setting.OPENROUTER_MODEL,
                "messages": messages,
                "stream": True,
            },
            timeout=api_setting.REQUEST_TIMEOUT,
            stream=True,  # <-- required client-side, or requests buffers the whole body
        ) as response:
            response.raise_for_status()

            for raw_line in response.iter_lines(decode_unicode=True):
                if not raw_line or not raw_line.startswith("data: "):
                    continue

                data = raw_line[len("data: "):]
                if data.strip() == "[DONE]":
                    break

                try:
                    chunk = json.loads(data)
                except json.JSONDecodeError:
                    logger.warning("Skipping malformed stream chunk: %s", data[:200])
                    continue

                delta = chunk.get("choices", [{}])[0].get("delta", {})
                content = delta.get("content")
                if content:
                    yield content

    except requests.exceptions.Timeout as e:
        raise OpenRouterError("OpenRouter stream timed out") from e
    except requests.exceptions.HTTPError as e:
        raise OpenRouterError(f"OpenRouter returned {e.response.status_code}") from e
    except requests.exceptions.RequestException as e:
        raise OpenRouterError("Failed to reach OpenRouter") from e
