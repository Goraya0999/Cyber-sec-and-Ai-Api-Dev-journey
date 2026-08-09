# ============================================
# #029 How do you use UploadFile with async streaming?
# ============================================

from fastapi import FastAPI, UploadFile, File

app = FastAPI()


@app.post("/stream")
async def stream_upload(file: UploadFile = File(...)):
    # UploadFile uses SpooledTemporaryFile internally
    # → Efficient for large files (stored in memory first, then disk)

    total_bytes = 0

    # Read file in chunks (streaming approach)
    # This avoids loading entire file into memory
    while True:
        chunk = await file.read(1024)  # read 1KB at a time

        if not chunk:
            # End of file reached
            break

        total_bytes += len(chunk)

    # IMPORTANT:
    # After reading, file pointer is at the end
    # If you want to re-read → use: await file.seek(0)

    return {"total_bytes": total_bytes}


# ============================================
# PROFESSIONAL NOTES (INLINE STYLE)
# ============================================

# - UploadFile is preferred over bytes for large files
#     bytes → loads entire file into memory ❌
#     UploadFile → streaming + efficient ✅
#
# - await file.read(size):
#     - Reads file asynchronously in chunks
#
# - Streaming is important for:
#     - Large file uploads (videos, PDFs, datasets)
#     - Preventing memory overflow
#
# - You can also write chunks directly to disk:
#
#     with open("output.bin", "wb") as f:
#         while chunk := await file.read(1024):
#             f.write(chunk)
#
# - Always consider file size limits in production
#
# ============================================



# ============================================
# #030 How do you get the filename and content type from an UploadFile?
# ============================================

from fastapi import UploadFile


@app.post("/info")
async def file_info(file: UploadFile = File(...)):
    # UploadFile provides metadata about uploaded file

    return {
        # Original filename sent by client
        "filename": file.filename,

        # MIME type (Content-Type header of file)
        # Example: "text/plain", "image/png", "application/pdf"
        "content_type": file.content_type
    }


# ============================================
# PROFESSIONAL NOTES (INLINE STYLE)
# ============================================

# - file.filename:
#     - Comes from client → NOT trusted
#     - Always sanitize before saving to disk
#
# - file.content_type:
#     - Provided by client → can be spoofed
#     - Do NOT rely on it for security-critical validation
#
# - Better validation:
#     - Check file signature (magic bytes)
#     - Use libraries like python-magic
#
# - Example validation:
#
#     if file.content_type not in ["image/png", "image/jpeg"]:
#         raise HTTPException(status_code=400, detail="Invalid file type")
#
# - You can also access raw file object:
#     file.file  → SpooledTemporaryFile (sync operations)
#
# - Always limit:
#     - File size
#     - Allowed types
#
# ============================================