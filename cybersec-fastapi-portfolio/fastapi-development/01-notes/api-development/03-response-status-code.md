# HTTP Response Status Codes Cheat Sheet

## What Are HTTP Status Codes?

HTTP status codes are three-digit numbers returned by a server to indicate the result of a client's request.

They help clients understand whether a request was successful, failed, redirected, or encountered an error.

---

# Status Code Categories

| Range | Category      | Meaning                                   |
| ----- | ------------- | ----------------------------------------- |
| 1xx   | Informational | Request received and processing continues |
| 2xx   | Success       | Request completed successfully            |
| 3xx   | Redirection   | Additional action is required             |
| 4xx   | Client Error  | Problem with the client's request         |
| 5xx   | Server Error  | Problem occurred on the server            |

---

# 1xx Informational Responses

These codes indicate that the request was received and processing has started.

| Code | Name                | Meaning                             |
| ---- | ------------------- | ----------------------------------- |
| 100  | Continue            | Client can continue sending request |
| 101  | Switching Protocols | Server is changing protocols        |
| 102  | Processing          | Request is being processed          |

---

# 2xx Success Responses

These codes indicate that the request was successfully received, understood, and processed.

## 200 OK

### Meaning

The request succeeded.

### Common Usage

* Successful GET request
* Successful API response

```http
GET /users
```

Response:

```http
200 OK
```

---

## 201 Created

### Meaning

A new resource was successfully created.

### Common Usage

* User registration
* Creating records
* Adding products

```http
POST /users
```

Response:

```http
201 Created
```

---

## 202 Accepted

### Meaning

The server accepted the request but has not completed processing yet.

### Common Usage

* Background jobs
* Queue processing

---

## 204 No Content

### Meaning

Request succeeded but no content is returned.

### Common Usage

* Successful DELETE request
* Successful update without response body

```http
DELETE /users/1
```

Response:

```http
204 No Content
```

---

# 3xx Redirection Responses

These codes indicate that the requested resource has moved or additional action is required.

## 301 Moved Permanently

### Meaning

Resource has permanently moved to a new URL.

### Common Usage

* Website migration
* URL changes

---

## 302 Found

### Meaning

Resource is temporarily available at another URL.

---

## 304 Not Modified

### Meaning

The resource has not changed since the last request.

### Common Usage

* Browser caching
* Performance optimization

---

# 4xx Client Error Responses

These codes indicate that the client sent an invalid or unauthorized request.

## 400 Bad Request

### Meaning

The request contains invalid syntax or missing data.

### Common Causes

* Invalid JSON
* Missing parameters
* Incorrect request format

---

## 401 Unauthorized

### Meaning

Authentication is required.

### Common Causes

* Missing token
* Invalid token
* Expired token

---

## 403 Forbidden

### Meaning

Authentication succeeded but access is denied.

### Common Causes

* Insufficient permissions
* Restricted resources

---

## 404 Not Found

### Meaning

Requested resource does not exist.

### Common Causes

* Invalid endpoint
* Missing resource

```http
GET /users/999
```

Response:

```http
404 Not Found
```

---

## 405 Method Not Allowed

### Meaning

The HTTP method is not allowed for the resource.

### Example

```http
DELETE /login
```

Response:

```http
405 Method Not Allowed
```

---

## 408 Request Timeout

### Meaning

The client took too long to send the request.

---

## 409 Conflict

### Meaning

The request conflicts with existing data.

### Common Causes

* Duplicate username
* Duplicate email

---

## 413 Payload Too Large

### Meaning

Request body exceeds the server limit.

### Common Causes

* Large file uploads

---

## 415 Unsupported Media Type

### Meaning

The server does not support the provided content type.

### Example

```http
Content-Type: text/plain
```

When JSON is expected.

---

## 422 Unprocessable Entity

### Meaning

Request format is valid but data validation failed.

### Common Causes

* Invalid email format
* Weak password
* Invalid field values

### API Testing Importance

Very common in REST APIs.

---

## 429 Too Many Requests

### Meaning

The client exceeded the allowed request limit.

### Common Causes

* Rate limiting
* API abuse protection

---

# 5xx Server Error Responses

These codes indicate that the server failed to process a valid request.

## 500 Internal Server Error

### Meaning

Generic server-side error.

### Common Causes

* Application crash
* Unhandled exception
* Database failure

---

## 501 Not Implemented

### Meaning

The server does not support the requested functionality.

---

## 502 Bad Gateway

### Meaning

Server received an invalid response from another server.

### Common Usage

* Reverse proxies
* Load balancers

---

## 503 Service Unavailable

### Meaning

Server is temporarily unavailable.

### Common Causes

* Maintenance
* Heavy traffic
* Server overload

---

## 504 Gateway Timeout

### Meaning

The server waited too long for another server to respond.

---

# Most Important Status Codes for REST APIs

| Code | Name                  |
| ---- | --------------------- |
| 200  | OK                    |
| 201  | Created               |
| 204  | No Content            |
| 400  | Bad Request           |
| 401  | Unauthorized          |
| 403  | Forbidden             |
| 404  | Not Found             |
| 405  | Method Not Allowed    |
| 409  | Conflict              |
| 422  | Unprocessable Entity  |
| 429  | Too Many Requests     |
| 500  | Internal Server Error |
| 502  | Bad Gateway           |
| 503  | Service Unavailable   |
| 504  | Gateway Timeout       |

---

# Status Codes Every API Pentester Must Know

| Code | Why Important                       |
| ---- | ----------------------------------- |
| 200  | Request succeeded                   |
| 201  | Resource created                    |
| 401  | Authentication issue                |
| 403  | Authorization issue                 |
| 404  | Resource discovery                  |
| 405  | Method testing                      |
| 409  | Business logic testing              |
| 422  | Input validation testing            |
| 429  | Rate limit testing                  |
| 500  | Server-side vulnerability indicator |
| 503  | Service availability issue          |

---

# Quick Memorization

```text
1xx → Information

2xx → Success

3xx → Redirection

4xx → Client Error

5xx → Server Error
```
