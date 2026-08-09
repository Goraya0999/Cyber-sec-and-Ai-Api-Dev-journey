from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.types import ASGIApp

# Swagger UI (/docs), ReDoc (/redoc), and Scalar (/scalar) all pull their
# JS/CSS/images from CDNs and use inline scripts/styles to render. A
# default-src 'none' CSP — which is exactly right for the JSON API itself —
# blocks all of that. These paths get a relaxed, docs-only CSP instead.
_DOCS_PATHS = {"/docs", "/redoc", "/scalar"}
_DOCS_PREFIXES = ("/docs", "/redoc")  # Swagger/ReDoc also load sub-resources

_DOCS_CSP = (
    "default-src 'self'; "
    "script-src 'self' 'unsafe-inline' cdn.jsdelivr.net; "
    "style-src 'self' 'unsafe-inline' cdn.jsdelivr.net fonts.googleapis.com; "
    "img-src 'self' data: fastapi.tiangolo.com cdn.jsdelivr.net; "
    "font-src 'self' fonts.gstatic.com data:; "
    "connect-src 'self'"
)
_API_CSP = "default-src 'none'; frame-ancestors 'none'"


class SecurityHeadersMiddleware(BaseHTTPMiddleware):
    def __init__(self, app: ASGIApp) -> None:
        super().__init__(app)

    async def dispatch(self, request: Request, call_next):
        response = await call_next(request)

        is_docs_route = request.url.path in _DOCS_PATHS or request.url.path.startswith(
            _DOCS_PREFIXES
        )

        response.headers["X-Content-Type-Options"] = "nosniff"
        response.headers["X-Frame-Options"] = "DENY"
        response.headers["Strict-Transport-Security"] = "max-age=63072000; includeSubDomains"
        response.headers["Referrer-Policy"] = "no-referrer"
        response.headers["Content-Security-Policy"] = _DOCS_CSP if is_docs_route else _API_CSP

        return response
