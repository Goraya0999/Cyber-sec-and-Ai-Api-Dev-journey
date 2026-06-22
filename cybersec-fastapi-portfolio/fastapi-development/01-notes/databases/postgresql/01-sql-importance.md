# Why Use SQL Databases Instead of JSON Files?

## What is a JSON File?

A **JSON (JavaScript Object Notation)** file is a lightweight text file used to store data as **key-value pairs**.

It is commonly used to exchange data between applications and APIs.

Example:

```json
[
    {
        "id": 1,
        "content": "Laptop",
        "weight": 10
    },
    {
        "id": 2,
        "content": "Books",
        "weight": 5
    }
]
```

---

# What is a SQL Database?

A **SQL (Structured Query Language) database** is a structured system used to store, organize, manage, and retrieve data efficiently.

Unlike JSON files, SQL databases organize data into **tables** with predefined columns and data types.

Examples of SQL databases include:

- MySQL
- PostgreSQL
- SQLite
- Microsoft SQL Server
- Oracle Database

---

# Why Do We Need SQL Databases?

As applications grow, storing data in JSON files becomes inefficient.

SQL databases solve problems related to:

- Large amounts of data
- Fast searching
- Data validation
- Data consistency
- Multiple users
- Security
- Scalability

---

# JSON File Storage

```text
JSON File
│
├── Shipment 1
├── Shipment 2
├── Shipment 3
├── Shipment 4
└── Shipment 5
```

To find one shipment, the application may need to search through the file.

---

# SQL Database Storage

```text
Database
    │
    ▼
 Shipments Table
 ┌────┬──────────┬────────┐
 │ ID │ Content  │ Weight │
 ├────┼──────────┼────────┤
 │ 1  │ Laptop   │ 10     │
 │ 2  │ Books    │ 5      │
 └────┴──────────┴────────┘
```

Data is stored in an organized structure, making retrieval much faster.

---

# JSON File vs SQL Database

| Feature | JSON File | SQL Database |
|---------|-----------|--------------|
| Storage | Text file | Structured database |
| Organization | Unstructured | Tables and columns |
| Search Speed | Slow for large data | Fast |
| Validation | Very limited | Strong validation |
| Relationships | Not supported | Supported |
| Multiple Users | Difficult | Fully supported |
| Security | Limited | Advanced |
| Scalability | Poor | Excellent |

---

# Problems with JSON Files

## 1. Slow Searching

To find one record, the application often needs to read the entire file.

As the file grows, searching becomes slower.

---

## 2. No Data Validation

JSON does not enforce rules.

Invalid data can easily be stored.

Example:

```json
{
    "weight": "Heavy"
}
```

A numeric value was expected, but a string was stored.

---

## 3. Difficult Updates

Updating one record usually requires:

- Reading the entire file.
- Modifying the data.
- Writing the entire file again.

---

## 4. Poor Performance

Large JSON files consume more memory and take longer to process.

---

## 5. No Relationships

JSON files cannot easily represent relationships between different types of data.

Example:

- Users
- Orders
- Products

Managing these relationships becomes complex.

---

## 6. Multi-User Issues

If multiple users try to modify the same JSON file simultaneously, data corruption may occur.

---

# Advantages of SQL Databases

## Organized Storage

Data is stored in rows and columns.

---

## Fast Searching

SQL databases use indexes and optimized search algorithms to retrieve records quickly.

---

## Data Validation

Each column has a defined data type.

Example:

```text
Weight → FLOAT
Content → VARCHAR
```

Invalid values are rejected.

---

## Data Integrity

Rules ensure that stored data remains accurate and consistent.

---

## Relationships

SQL databases can connect related tables.

Example:

```text
Customers
     │
     ▼
 Orders
     │
     ▼
 Products
```

---

## Security

SQL databases provide:

- User authentication
- Access control
- Permissions
- Encryption

---

## Concurrent Access

Many users can read and write data simultaneously without corrupting the database.

---

## Scalability

SQL databases efficiently manage millions of records.

---

# SQL Database Structure

```text
Database
   │
   ▼
Tables
   │
   ▼
Rows (Records)
   │
   ▼
Columns (Fields)
```

---

# Database Terminology

## Database

A collection of related tables.

---

## Table

A structured collection of related data.

Example:

```text
Shipments
```

---

## Row (Record)

A single entry in a table.

Example:

```text
ID: 1
Content: Laptop
Weight: 10
```

---

## Column (Field)

A property of every record.

Example:

```text
ID
Content
Weight
Status
```

---

# Example Table

| ID | Content | Weight | Status |
|----|----------|--------|---------|
| 1 | Laptop | 10 | Placed |
| 2 | Books | 5 | Delivered |
| 3 | Phone | 2 | Shipped |

---

# How Data is Retrieved

```text
Application
      │
      ▼
SQL Query
      │
      ▼
Database
      │
      ▼
Matching Rows
      │
      ▼
Application
```

---

# Why FastAPI Uses SQL Databases

FastAPI applications often require:

- Permanent data storage.
- Fast queries.
- Reliable updates.
- Multiple users.
- Data consistency.
- Secure storage.

SQL databases provide these features efficiently.

---

# JSON File vs SQL Workflow

## JSON

```text
Application
      │
      ▼
Read Entire File
      │
      ▼
Search Data
      │
      ▼
Modify Data
      │
      ▼
Write Entire File
```

---

## SQL Database

```text
Application
      │
      ▼
SQL Query
      │
      ▼
Database
      │
      ▼
Required Record Only
      │
      ▼
Return Result
```

---

# When to Use JSON Files

- Small projects.
- Configuration files.
- Static data.
- Temporary storage.
- API responses.

---

# When to Use SQL Databases

- Web applications.
- REST APIs.
- Banking systems.
- E-commerce websites.
- Inventory management.
- Hospital systems.
- School management systems.
- Enterprise software.

---

# Advantages of SQL Databases

- Organized data storage.
- Fast searching.
- Data validation.
- High performance.
- Data integrity.
- Secure access.
- Supports multiple users.
- Easy data relationships.
- Highly scalable.

---

# Limitations of JSON Files

- Slow with large datasets.
- No built-in validation.
- Difficult updates.
- No relationships.
- Weak security.
- Poor scalability.
- High memory usage.

---

# Important Terms

| Term | Definition |
|------|------------|
| JSON | JavaScript Object Notation, a lightweight text format for storing and exchanging data. |
| SQL | Structured Query Language used to manage relational databases. |
| Database | A structured collection of related data. |
| Table | A collection of related rows and columns. |
| Row (Record) | A single entry in a table. |
| Column (Field) | A specific attribute of every record in a table. |
| Data Validation | Ensuring stored data follows predefined rules. |
| Data Integrity | Maintaining accurate and consistent data. |
| Relationship | A connection between tables using related data. |
| Scalability | The ability to handle increasing amounts of data efficiently. |
| Concurrent Access | Allowing multiple users to access and modify data simultaneously. |
