# FastAPI Installation and Virtual Environment Setup on Linux

## Prerequisites

Verify that Python is installed:

```bash
python3 --version
```

Verify that pip is installed:

```bash
pip3 --version
```

If Python or pip is not installed:

### Ubuntu / Debian

```bash
sudo apt update
sudo apt install python3 python3-pip python3-venv -y
```

### Kali Linux

```bash
sudo apt update
sudo apt install python3 python3-pip python3-venv -y
```

---

# Step 1: Create a Project Directory

Create a new folder for your FastAPI project:

```bash
mkdir fastapi-project
```

Move into the project directory:

```bash
cd fastapi-project
```

---

# Step 2: Create a Virtual Environment

## What is a Virtual Environment?

A virtual environment is an isolated Python environment.

It allows each project to have its own:

* Packages
* Dependencies
* Versions

without affecting the system-wide Python installation.

Create a virtual environment:

```bash
python3 -m venv venv
```

### Command Breakdown

| Part    | Meaning                            |
| ------- | ---------------------------------- |
| python3 | Runs Python                        |
| -m      | Runs a Python module               |
| venv    | Virtual environment module         |
| venv    | Name of virtual environment folder |

---

# Step 3: Activate the Virtual Environment

Activate the environment:

```bash
source venv/bin/activate
```

Successful activation:

```bash
(venv) user@linux:~/fastapi-project$
```

The `(venv)` prefix indicates that the virtual environment is active.

---

# Step 4: Upgrade pip

Upgrade pip before installing packages:

```bash
pip install --upgrade pip
```

Verify version:

```bash
pip --version
```

---

# Step 5: Install FastAPI

Install FastAPI:

```bash
pip install fastapi
```

Verify installation:

```bash
pip show fastapi
```

---

# Step 6: Install Uvicorn

## What is Uvicorn?

Uvicorn is an ASGI server used to run FastAPI applications.

Install Uvicorn:

```bash
pip install uvicorn
```

Recommended installation:

```bash
pip install "uvicorn[standard]"
```

Verify installation:

```bash
uvicorn --version
```

---

# Step 7: Create the Application File

Create a Python file:

```bash
touch main.py
```

Project structure:

```text
fastapi-project/
│
├── venv/
│
└── main.py
```

---

# Step 8: Write Your First FastAPI Application

Open the file:

```bash
nano main.py
```

Add the following code:

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello FastAPI"}
```

Save and exit.

---

# Step 9: Start the FastAPI Server

Run:

```bash
uvicorn main:app --reload
```

### Command Breakdown

| Part     | Meaning                                 |
| -------- | --------------------------------------- |
| uvicorn  | ASGI server                             |
| main     | Python file name                        |
| app      | FastAPI application object              |
| --reload | Automatically reloads when code changes |

---

# Step 10: Verify the Server

Terminal output:

```text
INFO: Uvicorn running on http://127.0.0.1:8000
```

Open:

```text
http://127.0.0.1:8000
```

Expected response:

```json
{
  "message": "Hello FastAPI"
}
```

---

# Step 11: Access Swagger Documentation

FastAPI automatically generates interactive API documentation.

Open:

```text
http://127.0.0.1:8000/docs
```

Features:

* Test API endpoints
* View request parameters
* View responses
* Execute requests directly from browser

---

# Step 12: Access ReDoc Documentation

Open:

```text
http://127.0.0.1:8000/redoc
```

Provides:

* Clean API documentation
* Structured endpoint information
* Professional API reference

---

# Step 13: View Installed Packages

List installed packages:

```bash
pip list
```

---

# Step 14: Create requirements.txt

Generate dependency file:

```bash
pip freeze > requirements.txt
```

Project structure:

```text
fastapi-project/
│
├── venv/
├── main.py
└── requirements.txt
```

View dependencies:

```bash
cat requirements.txt
```

---

# Step 15: Install Dependencies from requirements.txt

When cloning the project later:

```bash
pip install -r requirements.txt
```

---

# Step 16: Deactivate Virtual Environment

Exit virtual environment:

```bash
deactivate
```

Prompt changes from:

```text
(venv) user@linux:~$
```

to:

```text
user@linux:~$
```

---

# Step 17: Reactivate Virtual Environment Later

Navigate to project:

```bash
cd fastapi-project
```

Activate:

```bash
source venv/bin/activate
```

Run server:

```bash
uvicorn main:app --reload
```

---

# Complete Setup Commands

```bash
sudo apt update

sudo apt install python3 python3-pip python3-venv -y

mkdir fastapi-project

cd fastapi-project

python3 -m venv venv

source venv/bin/activate

pip install --upgrade pip

pip install fastapi

pip install "uvicorn[standard]"

touch main.py

uvicorn main:app --reload
```

---

# Minimum Packages Required

```bash
pip install fastapi

pip install "uvicorn[standard]"
```

These two packages are sufficient to start building and testing FastAPI applications.
