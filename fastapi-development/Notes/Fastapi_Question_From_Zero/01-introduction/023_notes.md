# 🔹 #050 — What Happens When You Define Two Routes with the Same Path in FastAPI?

---

## 📖 Overview

In **FastAPI**, if you define **multiple routes with the same path**, the framework will **use the first matching route**.

> 📌 **Order of route definition matters** — the first match wins.

---

## 🧠 How It Works

- FastAPI processes routes **top to bottom**
- When a request comes in:
  - It finds the **first matching route**
  - Ignores the rest ❌

---

## 🔧 Example

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/items/{item_id}")
def get_item(item_id: int):
    return {"item_id": item_id}

@app.get("/items/special")
def get_special():
    return {"message": "Special item"}