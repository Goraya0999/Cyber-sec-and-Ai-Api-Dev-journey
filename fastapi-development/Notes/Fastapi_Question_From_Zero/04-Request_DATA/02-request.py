#004 How do you handle file uploads in FastAPI?

# Use File() and UploadFile to accept file uploads

from fastapi import FastAPI, File, UploadFile

app = FastAPI()


@app.post("/upload")
async def upload(file: UploadFile = File(...)):
    """
    FastAPI will:
        ✔ Accept file from request (multipart/form-data)
        ✔ Provide file metadata (filename, content_type)
        ✔ Allow async file handling
    """

    content = await file.read()   # Read file content

    return {
        "filename": file.filename,
        "size": len(content)
    }


# Example Request:
"""
POST /upload
Content-Type: multipart/form-data

file = (binary file)
"""


#-------------------------


#005 What is the difference between File() and UploadFile?

# Two ways to handle files:

"""
1. File() with bytes:
    file: bytes = File(...)

    ✔ Reads entire file into memory
    ✔ Simple to use
    ❌ Not suitable for large files (memory heavy)


2. UploadFile:
    file: UploadFile = File(...)

    ✔ Uses SpooledTemporaryFile (disk-backed)
    ✔ Efficient for large files
    ✔ Supports async operations:
        - await file.read()
        - await file.seek()
        - await file.close()
    ✔ Provides metadata:
        - file.filename
        - file.content_type


Professional Recommendation:
    👉 Use UploadFile in real applications
    👉 Use bytes only for small files or quick testing
"""

#-------------------------------
#006 How do you handle multiple file uploads?

# Use List[UploadFile] with File() to accept multiple files

from fastapi import FastAPI, File, UploadFile
from typing import List

app = FastAPI()


@app.post("/upload-many")
async def upload_many(files: List[UploadFile] = File(...)):
    """
    FastAPI will:
        ✔ Accept multiple files under same field name
        ✔ Provide list of UploadFile objects
        ✔ Allow async processing for each file
    """

    filenames = []

    for file in files:
        # You can process each file individually
        content = await file.read()

        filenames.append({
            "filename": file.filename,
            "size": len(content)
        })

    return filenames


# Example Request:
"""
POST /upload-many
Content-Type: multipart/form-data

files = file1.jpg
files = file2.pdf
files = file3.png
"""


# Professional Insight:
# ✔ Use UploadFile for scalability (large files)
# ✔ Always validate file type/size in production
# ✔ Consider streaming instead of reading full file for very large uploads