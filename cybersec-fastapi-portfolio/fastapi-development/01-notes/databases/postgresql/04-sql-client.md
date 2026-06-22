# Running SQL Commands and Connecting to a PostgreSQL Server

## Introduction

Before writing SQL queries like `SELECT`, `INSERT`, or `UPDATE`, you need to understand **how SQL commands reach the database**.

Many beginners think SQL runs directly on their computer, but in reality, SQL follows a **Client-Server Architecture**.

The **client** sends SQL commands to the **database server**, and the **server** processes those commands and returns the results.

Understanding this communication makes it much easier to learn SQL and databases.

---

# Client-Server Architecture

## What is a Client?

A **client** is a program that allows users to communicate with a database server.

It is responsible for:

- Sending SQL commands
- Receiving results
- Displaying output to the user

### Examples

- `psql` (PostgreSQL Command Line Client)
- pgAdmin
- DBeaver
- Python programs using PostgreSQL libraries
- Web applications

---

## What is a Database Server?

A **database server** is software that stores, manages, and retrieves data.

It performs all the heavy work behind the scenes, such as:

- Storing data on disk
- Managing memory
- Processing SQL queries
- Optimizing performance
- Handling multiple users simultaneously
- Enforcing security permissions

You simply send SQL commands—the server does all the complex work.

---

# Client-Server Communication

```text
             SQL Command
                  │
                  ▼
        +----------------+
        |     Client     |
        | (psql, pgAdmin)|
        +----------------+
                  │
                  │ Sends SQL
                  ▼
        +----------------------+
        | PostgreSQL Server    |
        | Stores & Processes   |
        | Database             |
        +----------------------+
                  │
                  │ Returns Result
                  ▼
        +----------------+
        |     Client     |
        +----------------+
```

---

# Important Concept

Even if both the client and server are installed on the **same computer**, they are still **two different pieces of software**.

For example:

```text
Your Laptop

+-------------------------+
| PostgreSQL Server       |
+-------------------------+

+-------------------------+
| psql Client             |
+-------------------------+
```

The client communicates with the server exactly the same way it would if the server were on another computer.

---

# Why Use a Database Server?

Database servers have been developed and optimized by experienced software engineers over many years.

They handle difficult tasks such as:

- Fast searching
- Efficient storage
- Data caching
- Concurrency (multiple users)
- Transactions
- Recovery after crashes
- Security

Instead of writing all this yourself, you simply use SQL.

---

# SQL Workflow

The overall workflow is simple.

```text
Write SQL
     │
     ▼
Client sends SQL
     │
     ▼
Database Server executes SQL
     │
     ▼
Result is returned
```

---

# PostgreSQL Clients

There are many ways to communicate with PostgreSQL.

| Client | Description |
|---------|-------------|
| `psql` | Command-line client |
| pgAdmin | Web-based graphical interface |
| DBeaver | Desktop database management tool |
| Python Programs | Applications using PostgreSQL libraries |

All of these perform the same job—they simply provide different interfaces.

---

# Why Learn the Command Line?

The instructor chooses **psql** because it offers several advantages.

## Advantages

- Lightweight
- Fast
- Works on any operating system
- Easy to document
- No screenshots required
- Accessible for visually impaired users
- Widely used by professionals

Everything you can do in pgAdmin can also be done using `psql`.

---

# Why Learn Linux?

Most production database servers run on Linux.

Even if you use:

- Windows
- macOS

the commands are very similar when using a terminal.

Learning Linux helps because:

- Most cloud servers use Linux.
- Most database servers run on Linux.
- Most cybersecurity professionals use Linux.
- Most DevOps engineers use Linux.

---

# Connecting to PostgreSQL

The PostgreSQL command-line client is called:

```bash
psql
```

When you connect, you provide:

- Database name
- Username
- Password

Example:

```bash
psql people pg4e
```

The client connects to the database server using these credentials.

---

# PostgreSQL Users

Every PostgreSQL server contains user accounts.

Each user has:

- Username
- Password
- Permissions

Different users can have different levels of access.

---

# Superuser

The first account created during PostgreSQL installation is usually:

```text
postgres
```

This account is called the **superuser**.

The superuser can:

- Create users
- Delete users
- Create databases
- Delete databases
- Change permissions
- Manage the entire server

It has complete control.

---

# Superuser Prompt

In PostgreSQL, the prompt often indicates whether you are a superuser.

Example:

```text
postgres=#
```

The `#` symbol generally indicates elevated privileges.

Regular users often see:

```text
people=>
```

---

# Linux sudo

Linux also has the idea of a superuser.

The command used to temporarily gain administrator privileges is:

```bash
sudo
```

Example:

```bash
sudo rm file.txt
```

Without `sudo`, Linux may refuse the operation because it requires administrator permissions.

---

# Why Avoid Using the Superuser?

Using the superuser for everyday work is risky.

If you make a mistake, you could accidentally:

- Delete databases
- Remove users
- Change permissions
- Damage the PostgreSQL installation

Best practice:

```text
Superuser
      │
      ▼
Create User
      │
      ▼
Create Database
      │
      ▼
Use Normal User for Daily Work
```

---

# Listing Databases

PostgreSQL command:

```sql
\l
```

This displays all databases available on the server.

Example output may include:

- postgres
- template0
- template1

These are system databases.

---

# Important Warning

Do **not** delete PostgreSQL's built-in databases.

Examples:

- postgres
- template0
- template1

These databases are required for PostgreSQL to function correctly.

Deleting them may break the database server.

---

# Creating a New User

SQL command:

```sql
CREATE USER pg4e
WITH PASSWORD 'secret';
```

This creates a new PostgreSQL account.

---

# Creating a Database

SQL command:

```sql
CREATE DATABASE people
WITH OWNER pg4e;
```

This creates a new database named `people`.

Ownership is assigned to the `pg4e` user.

---

# Exiting PostgreSQL

To quit the `psql` client:

```sql
\q
```

---

# Connecting as a Normal User

Instead of logging in as the superuser, connect using your own account.

Example:

```bash
psql people pg4e
```

Now you are working only inside your own database.

---

# Listing Tables

To display tables inside the current database:

```sql
\dt
```

Example output:

```text
Did not find any relations.
```

This simply means the database contains no tables yet.

---

# Relation vs Table

PostgreSQL often uses the word **relation**.

In practice:

| Database Term | Meaning |
|--------------|---------|
| Relation | Table |
| Table | Relation |

They refer to the same concept.

---

# Creating a Table

Example:

```sql
CREATE TABLE users (
    name VARCHAR(128),
    email VARCHAR(128)
);
```

This creates a table named `users`.

It contains two columns.

---

# Understanding the Schema

A **schema** defines the structure of a table.

It specifies:

- Column names
- Data types
- Constraints

Example:

```text
users

----------------------------
name    VARCHAR(128)
email   VARCHAR(128)
```

Think of the schema as a contract between you and PostgreSQL.

---

# Why Does PostgreSQL Enforce Data Types?

Suppose you define:

```sql
VARCHAR(128)
```

This means the column can store **up to 128 characters**.

If you try to insert:

```text
129 characters
```

PostgreSQL rejects it.

Why?

Because it stores data based on the rules you provided.

It optimizes storage and performance using those rules.

---

# Viewing Table Information

To display tables:

```sql
\dt
```

To display detailed table information:

```sql
\d+ users
```

This shows:

- Columns
- Data types
- Storage information
- Owner
- Constraints

---

# PostgreSQL Workflow

```text
Install PostgreSQL
        │
        ▼
Login as Superuser
        │
        ▼
Create User
        │
        ▼
Create Database
        │
        ▼
Login as Normal User
        │
        ▼
Create Tables
        │
        ▼
Insert Data
        │
        ▼
Read Data
        │
        ▼
Update Data
        │
        ▼
Delete Data
```

---

# Real-World Example

Imagine a university database.

## Superuser

Creates:

- Student accounts
- Faculty accounts
- Databases

---

## Student User

Can:

- View records
- Insert assignments
- Update personal information

Cannot:

- Delete the university database
- Create administrator accounts

This separation keeps the system secure.

---

# Common PostgreSQL Commands

| Command | Purpose |
|----------|---------|
| `psql` | Start PostgreSQL client |
| `\l` | List databases |
| `\dt` | List tables |
| `\d+ table_name` | Show table schema |
| `\q` | Quit PostgreSQL |
| `CREATE USER` | Create a new user |
| `CREATE DATABASE` | Create a new database |
| `CREATE TABLE` | Create a table |

---

# Key Takeaways

- PostgreSQL follows a **client-server architecture**.
- The **client** sends SQL commands to the **database server**.
- The database server performs all data processing.
- `psql` is PostgreSQL's command-line client.
- The **superuser** manages users, databases, and permissions.
- Everyday work should be done using a **normal user**, not the superuser.
- A **schema** defines the structure of a table.
- PostgreSQL enforces schemas to improve performance and maintain data integrity.
- Commands like `\l`, `\dt`, and `\d+` help inspect databases and tables.

---

# Interview Questions

## 1. What is the difference between a client and a database server?

A client sends SQL commands, while the database server processes those commands, manages data, and returns the results.

---

## 2. What is `psql`?

`psql` is PostgreSQL's command-line client used to connect to a PostgreSQL server and execute SQL commands.

---

## 3. What is a PostgreSQL superuser?

A superuser has complete administrative privileges, including creating users, databases, and managing permissions.

---

## 4. Why should you avoid using the superuser for daily work?

Using the superuser increases the risk of accidentally modifying or deleting important databases or server settings.

---

## 5. What is a schema?

A schema defines a table's structure, including its columns, data types, and constraints.

---

## 6. What does the `\dt` command do?

It lists all tables (relations) in the current database.

---

## 7. What does the `\d+` command do?

It displays detailed information about a table, including its schema, columns, and data types.

---

## 8. Why does PostgreSQL enforce data types like `VARCHAR(128)`?

It ensures data integrity and allows PostgreSQL to store and retrieve data efficiently based on the defined structure.

---


