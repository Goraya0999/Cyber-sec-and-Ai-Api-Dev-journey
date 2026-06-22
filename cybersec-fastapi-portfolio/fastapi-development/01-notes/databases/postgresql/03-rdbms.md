# Introduction to Relational Databases

## What is a Relational Database?

A **relational database** is software used to **store, organize, manage, and retrieve data efficiently**.

One of the most popular relational databases today is **PostgreSQL (Postgres)** because it is:

- Free and open source
- Fast and reliable
- Feature-rich
- Scalable for small and large applications

---

# Why Are Databases Important?

Every day, we use applications that rely on databases.

Examples include:

- Learning Management Systems (LMS)
- Banking applications
- Social media
- E-commerce websites
- Online games

When you log in, the system instantly retrieves information like:

- Your profile
- Your password (hashed)
- Your notifications
- Your courses
- Your orders

Even if the database contains **terabytes of data**, modern databases can find your information in **milliseconds**.

---

# Before Databases Existed

Before modern databases, organizations stored data on **magnetic tapes**.

### Problems with Magnetic Tape

Magnetic tape stored data **sequentially (one after another).**

Example:

```
Account 1
Account 2
Account 3
...
Account 1,000,000
```

If you wanted to read **Account 900,000**, the computer had to pass through almost every previous record.

This made searching extremely slow.

---

# Sequential Master Update

Banks used a process called the **Sequential Master Update**.

## How it Worked

### Step 1

Customer performs a transaction.

Examples:

- Deposit money
- Withdraw money

---

### Step 2

The transaction is recorded separately.

Example:

| Account | Transaction |
|----------|------------|
|1005|+500|
|2050|-100|
|4500|+1000|

---

### Step 3

At the end of the day:

- Transactions were sorted by account number.
- The old master data was also sorted.

---

### Step 4

A program merged both files.

Old Data

```
1001
1002
1003
1004
1005
```

Transactions

```
1005 +500
```

New Master File

```
1001
1002
1003
1004
1005 (+500)
```

---

### Advantages

- Very little memory required
- Simple process

### Disadvantages

- Updates only happened once per day
- Searching was slow
- Not suitable for real-time applications

---

# The Arrival of Disk Drives

Later, magnetic tapes were replaced by:

- Hard Disk Drives (HDD)
- Solid State Drives (SSD)

Unlike tape, disks allow **random access**.

Instead of reading everything in order, the computer can jump directly to the required data.

Example:

Instead of

```
1 → 2 → 3 → ... → 900000
```

It can go directly to

```
900000
```

This dramatically improved performance.

---

# Birth of Relational Databases

Once hard drives became common, computer scientists designed software that could:

- Store data efficiently
- Search quickly
- Update instantly
- Handle millions of records

This software became known as the **Relational Database Management System (RDBMS).**

Examples include:

- PostgreSQL
- MySQL
- Oracle Database
- Microsoft SQL Server
- SQLite

---

# Why Are Relational Databases Fast?

Modern databases use advanced techniques such as:

- Indexing
- Data structures
- Query optimization
- Mathematical algorithms

Instead of scanning every record, they quickly locate the required data.

This is why databases can search billions of records in milliseconds.

---

# Database Standardization

In the early days, every company built its own database.

Examples:

- IBM Database
- Burroughs Database
- Oracle Database

Each used different commands.

This made it difficult for developers.

To solve this, the **National Institute of Standards and Technology (NIST)** helped create a common language called **SQL (Structured Query Language).**

Today, almost every relational database supports SQL.

---

# What is SQL?

SQL stands for:

**Structured Query Language**

SQL is the standard language used to communicate with relational databases.

Instead of telling the computer **how** to find data, you simply tell it **what** data you need.

The database decides the fastest way to retrieve it.

---

# Procedural vs Non-Procedural Languages

## Procedural Language

A procedural language tells the computer every step.

Example:

```
Open table
Read first row
Check condition
Go to next row
Repeat
```

Languages like:

- C
- C++
- Python
- Java

are procedural.

---

## Non-Procedural Language

SQL is **non-procedural**.

You simply write:

```sql
SELECT * FROM students;
```

You don't tell the database:

- Which row to read first
- Which algorithm to use
- Which index to use

The database automatically chooses the fastest method.

---

# CRUD Operations

Every database mainly performs four operations.

| Operation | Meaning |
|------------|---------|
|Create|Insert new data|
|Read|Retrieve data|
|Update|Modify existing data|
|Delete|Remove data|

CRUD forms the foundation of database programming.

---

# Mathematical Foundation

Relational databases are based on **Relational Theory**, a branch of mathematics.

Database theory uses these formal terms:

| Database Theory | Common Name |
|-----------------|-------------|
|Relation|Table|
|Tuple|Row|
|Attribute|Column|

Example:

| Student_ID | Name | Age |
|------------|------|-----|
|101|Ali|20|

- Relation = Students table
- Tuple = One student record
- Attribute = Student_ID, Name, Age

---

# Think of a Database Like a Spreadsheet

A database is similar to a spreadsheet.

Spreadsheet

|ID|Name|Age|
|--|----|---|
|1|Ali|20|
|2|Sara|22|

Database

- Table = Spreadsheet
- Row = Record
- Column = Field

The difference is that databases are much faster, more secure, and designed to handle millions of records.

---

# Popular Database Systems

## PostgreSQL

- Open source
- Feature-rich
- Highly scalable
- Excellent for enterprise applications

---

## MySQL

- Popular for web development
- Open source
- Owned by Oracle

---

## Oracle Database

- Enterprise-grade
- Very powerful
- Commercial product
- Expensive
- Used by large organizations

---

## Microsoft SQL Server

- Developed by Microsoft
- Common in Windows environments
- Enterprise database

---

## SQLite

- Lightweight
- No server required
- Used in mobile and desktop applications

---

# Why Learn PostgreSQL?

PostgreSQL offers:

- Advanced SQL features
- Excellent performance
- JSON support
- Strong security
- Scalability
- Active open-source community

It is widely used in:

- Backend development
- APIs
- Cloud computing
- Enterprise software
- Data analytics

---

# Key Takeaways

- Relational databases store and organize data efficiently.
- Before databases, data was stored on magnetic tapes using sequential access.
- Hard drives enabled random access, making databases much faster.
- SQL became the standard language for communicating with databases.
- SQL is non-procedural—you describe **what** data you want, not **how** to retrieve it.
- CRUD (Create, Read, Update, Delete) is the foundation of database operations.
- PostgreSQL is one of the most powerful and feature-rich open-source relational databases.

---

# Interview Questions

### 1. What is a relational database?

A relational database stores data in tables consisting of rows and columns, allowing efficient storage, retrieval, and management of related data.

---

### 2. Why were magnetic tapes inefficient?

Because they only supported sequential access, meaning the computer had to read records one by one until it reached the desired data.

---

### 3. What is SQL?

SQL (Structured Query Language) is the standard language used to communicate with relational databases.

---

### 4. What does CRUD stand for?

- Create
- Read
- Update
- Delete

---

### 5. What is the difference between procedural and non-procedural programming?

Procedural programming tells the computer **how** to perform a task step by step, while non-procedural programming (like SQL) specifies **what** result is needed, letting the database determine the best execution plan.

---

### 6. Why is PostgreSQL popular?

Because it is:

- Open source
- Secure
- Fast
- Scalable
- Feature-rich
- Suitable for modern applications

---


