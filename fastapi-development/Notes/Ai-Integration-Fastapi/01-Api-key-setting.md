# #01 Secure API Key Storage with `pydantic_settings`

## Overview

When building applications that use APIs such as OpenAI or Anthropic, you need an API key.

An API key is a secret credential that allows your application to access a service.

**Never hardcode API keys directly in your source code.**

❌ Bad Example:

```python
OPENAI_API_KEY = "sk-123456789abcdef"
```

If you upload your code to GitHub, anyone can see and misuse your API key.

✅ Good Example:

Store the API key in a `.env` file and load it using `pydantic_settings`.

---

# Why Use `pydantic_settings`?

`pydantic_settings` helps you:

- Read configuration from environment variables
- Keep secrets out of source code
- Validate required settings automatically
- Manage application configuration easily

---

# Step 1: Install Required Packages

```bash
pip install pydantic-settings python-dotenv
```

### Package Purpose

| Package | Purpose |
|----------|----------|
| pydantic-settings | Load settings from environment variables |
| python-dotenv | Read values from `.env` files |

---

# Step 2: Create Settings Class

```python
from pydantic_settings import BaseSettings
from functools import lru_cache

class Settings(BaseSettings):
    openai_api_key: str
    model: str = "gpt-4o-mini"
    debug: bool = False

    class Config:
        env_file = ".env"
```

---

# Understanding the Code

## BaseSettings

```python
class Settings(BaseSettings):
```

`BaseSettings` automatically loads values from:

- Environment variables
- `.env` files

Example:

```env
OPENAI_API_KEY=sk-abc123
```

becomes:

```python
settings.openai_api_key
```

---

## Required Field

```python
openai_api_key: str
```

This field is required.

If it is missing, the application will fail to start.

Example:

```env
OPENAI_API_KEY=sk-abc123
```

Loaded as:

```python
settings.openai_api_key
```

---

## Default Model

```python
model: str = "gpt-4o-mini"
```

If no model is provided, it uses:

```python
gpt-4o-mini
```

---

## Debug Mode

```python
debug: bool = False
```

Default value:

```python
False
```

Can be overridden:

```env
DEBUG=true
```

---

## Config Class

```python
class Config:
    env_file = ".env"
```

Tells Pydantic:

> Read environment variables from the `.env` file.

---

# Step 3: Create `.env` File

Create a file named:

```text
.env
```

Inside it:

```env
OPENAI_API_KEY=sk-your-api-key-here
```

Example:

```env
OPENAI_API_KEY=sk-abc123xyz
DEBUG=true
```

---

# Important Security Rule

Never upload `.env` to GitHub.

Add it to `.gitignore`.

Example:

```text
.env
```

---

# Step 4: Create Cached Settings Dependency

```python
@lru_cache
def get_settings() -> Settings:
    return Settings()
```

---

# What is `@lru_cache`?

`@lru_cache` stores the settings object in memory.

Without cache:

```python
Settings()
Settings()
Settings()
```

Settings are loaded repeatedly.

With cache:

```python
Settings()
```

Loaded only once and reused.

### Benefits

- Faster performance
- Less file reading
- Same settings object reused

---

# Step 5: Create Safe `/config` Route

Example:

```python
from fastapi import FastAPI, Depends

app = FastAPI()

@app.get("/config")
def get_config(settings: Settings = Depends(get_settings)):
    return {
        "model": settings.model,
        "debug": settings.debug
    }
```

---

# Response Example

Request:

```http
GET /config
```

Response:

```json
{
  "model": "gpt-4o-mini",
  "debug": false
}
```

---

# Why Is This Safe?

Only non-sensitive fields are returned.

Returned:

```json
{
  "model": "gpt-4o-mini",
  "debug": false
}
```

Not returned:

```json
{
  "openai_api_key": "sk-abc123"
}
```

---

# Never Do This

❌ Dangerous:

```python
@app.get("/config")
def get_config(settings: Settings = Depends(get_settings)):
    return settings.model_dump()
```

Why?

Because it exposes:

```json
{
  "openai_api_key": "sk-abc123"
}
```

Anyone can steal your API key.

---

# Step 6: Verify Missing API Key Behavior

Suppose `.env` does not contain:

```env
OPENAI_API_KEY=...
```

When application starts:

```python
Settings()
```

Pydantic validation fails.

Example error:

```text
ValidationError:
openai_api_key
Field required
```

Application refuses to start.

This is good because:

- Missing configuration is detected early
- No unexpected runtime failures
- Clear error message for developers

---

# Extra Security Using `SecretStr`

Instead of:

```python
openai_api_key: str
```

Use:

```python
from pydantic import SecretStr

openai_api_key: SecretStr
```

Full Example:

```python
from pydantic import SecretStr
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    openai_api_key: SecretStr
```

---

# Why Use `SecretStr`?

Normal string:

```python
print(settings.openai_api_key)
```

Output:

```text
sk-abc123xyz
```

SecretStr:

```python
print(settings.openai_api_key)
```

Output:

```text
**********
```

The real key is hidden.

This reduces accidental exposure in logs.

---

# Complete Example

```python
from functools import lru_cache
from pydantic import SecretStr
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    openai_api_key: SecretStr
    model: str = "gpt-4o-mini"
    debug: bool = False

    class Config:
        env_file = ".env"

@lru_cache
def get_settings() -> Settings:
    return Settings()
```

---

# Interview Points

### What is `pydantic_settings`?

A library that loads application configuration from environment variables and `.env` files.

---

### Why should API keys not be hardcoded?

Because source code may be shared publicly, exposing secrets.

---

### Why use `.env` files?

To keep secrets separate from source code.

---

### What does `BaseSettings` do?

Automatically loads and validates environment variables.

---

### What is `@lru_cache` used for?

To create and reuse a single settings instance.

---

### Why use `SecretStr`?

To prevent API keys from appearing in logs and print statements.

---

### Should API keys be returned from API routes?

No. API keys should never be exposed to clients.

---

# Key Points Summary

- Store API keys in `.env` files.
- Never hardcode secrets in source code.
- Use `BaseSettings` to load configuration.
- Use `@lru_cache` for efficient settings reuse.
- Return only safe configuration values.
- Never expose API keys in API responses.
- Use `SecretStr` for extra protection.
- Missing required environment variables should stop application startup.
