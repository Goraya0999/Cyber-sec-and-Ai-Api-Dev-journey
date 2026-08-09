# 🔹 #044 — How to Run Multiple Uvicorn Workers

---

## 📖 Overview

When building FastAPI applications, running your app with **multiple workers** allows you to **handle more requests concurrently** and improve performance.

> 📌 **Workers = Separate processes** running your app in parallel

---

## 🚀 Basic Command

```bash
uvicorn main:app --workers 4
```
# 🔹 #045 — What is Gunicorn and How Does It Work with FastAPI?

---

## 📖 Overview

**Gunicorn** (Green Unicorn) is a **production-grade Python web server** used to run applications efficiently.

> 📌 By default, Gunicorn is a **WSGI server**, while FastAPI is **ASGI-based**

So how do they work together? 🤔  
👉 By using **Uvicorn workers**, Gunicorn can run FastAPI apps properly.

---

## 🧠 Key Concept

- **Gunicorn** → Manages multiple worker processes (process manager)  
- **Uvicorn** → Handles async requests (ASGI server)  
- **UvicornWorker** → Bridge between Gunicorn + FastAPI  

---

## 🚀 Run FastAPI with Gunicorn

```bash
gunicorn main:app -w 4 -k uvicorn.workers.UvicornWorker


JMCFQS6uj@8Ugdr