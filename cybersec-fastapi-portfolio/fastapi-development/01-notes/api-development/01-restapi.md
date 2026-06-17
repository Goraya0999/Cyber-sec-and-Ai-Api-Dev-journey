# REST API

## What is REST API?

- **REST** stands for **Representational State Transfer**.
- **API** stands for **Application Programming Interface**.
- A REST API is a set of rules that allows different applications to communicate over the internet using HTTP.
- It enables a client (browser, mobile app, script) to send requests to a server and receive responses.
- REST APIs are widely used in web applications, mobile applications, cloud services, and microservices.

## How REST API Works

1. The client sends an HTTP request to the server.
2. The request contains a URL (endpoint) and an HTTP method.
3. The server receives and processes the request.
4. The server may interact with a database if needed.
5. The server sends a response back to the client, usually in JSON format.

```text
Client
   │
   │ Request
   ▼
REST API Server
   │
   │ Process Request
   ▼
Database
   │
   │ Data
   ▼
REST API Server
   │
   │ Response (JSON)
   ▼
Client
