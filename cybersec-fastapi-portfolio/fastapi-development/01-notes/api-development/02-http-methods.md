# HTTP Methods

## Overview

HTTP methods are predefined actions used in the **HTTP (HyperText Transfer Protocol)** to specify what operation a client wants to perform on a resource available on a server.

When a client sends a request to a server, the HTTP method tells the server whether the client wants to retrieve data, create new data, update existing data, or delete data.

HTTP methods are a fundamental part of web development and REST APIs.

---

## GET Method

### What It Is

The `GET` method is used to retrieve data from a server.

### Why It Exists

Applications frequently need to read information stored on a server without changing it.

### How It Works

A client sends a GET request to a specific endpoint, and the server returns the requested data.

### Characteristics

* Used for reading data.
* Does not modify server data.
* Can be cached by browsers.
* Commonly used when viewing information.

### Example

```http
GET /users
```

---

## POST Method

### What It Is

The `POST` method is used to create a new resource on the server.

### Why It Exists

Applications need a way to send new information to the server for storage.

### How It Works

The client sends data in the request body, and the server creates a new resource using that data.

### Characteristics

* Used for creating data.
* Modifies server data.
* Data is sent in the request body.
* Commonly used in registration forms and data submission.

### Example

```http
POST /users
```

---

## PUT Method

### What It Is

The `PUT` method is used to replace an existing resource completely.

### Why It Exists

Applications sometimes need to update all information associated with a resource.

### How It Works

The client sends a complete representation of the resource, and the server replaces the existing resource with the new version.

### Characteristics

* Used for complete updates.
* Replaces all existing fields.
* Modifies server data.
* Requires the target resource identifier.

### Example

```http
PUT /users/1
```

---

## PATCH Method

### What It Is

The `PATCH` method is used to update specific parts of an existing resource.

### Why It Exists

Replacing an entire resource is often unnecessary when only a few fields need to change.

### How It Works

The client sends only the fields that need modification, and the server updates those fields while leaving the remaining data unchanged.

### Characteristics

* Used for partial updates.
* More efficient than PUT for small changes.
* Modifies server data.
* Updates only specified fields.

### Example

```http
PATCH /users/1
```

---

## DELETE Method

### What It Is

The `DELETE` method is used to remove a resource from the server.

### Why It Exists

Applications need a standard way to permanently remove information that is no longer required.

### How It Works

The client sends a DELETE request to a resource endpoint, and the server removes the targeted resource.

### Characteristics

* Used for deleting data.
* Modifies server data.
* Targets a specific resource.
* Commonly used in management systems and administrative operations.

### Example

```http
DELETE /users/1
```

---

## HTTP Methods Comparison

| Method | Purpose                 | Creates Data | Updates Data | Deletes Data |
| ------ | ----------------------- | ------------ | ------------ | ------------ |
| GET    | Retrieve data           | No           | No           | No           |
| POST   | Create data             | Yes          | No           | No           |
| PUT    | Replace data completely | No           | Yes          | No           |
| PATCH  | Update data partially   | No           | Yes          | No           |
| DELETE | Remove data             | No           | No           | Yes          |

---

## Real-World Applications

### GET

* Viewing user profiles
* Reading product information
* Loading web pages

### POST

* User registration
* Creating orders
* Submitting forms

### PUT

* Updating complete user profiles
* Replacing product information

### PATCH

* Changing passwords
* Updating email addresses
* Editing specific settings

### DELETE

* Removing user accounts
* Deleting products
* Removing comments
