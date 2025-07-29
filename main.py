from fastapi import FastAPI, File, UploadFile
from pydantic import BaseModel
import os
import shutil
import pdfplumber

app = FastAPI()
uploadPath = "uploads"
os.makedirs(uploadPath, exist_ok=True)

class Register(BaseModel):
    name : str
    email: str
    password: str
    
class Pdfreader(BaseModel):
    file:str

@app.get("/home")
def home():
    return {
        "message": "Welcome to world"
    }

@app.post("/register")
def register(User: Register):
    return {
        "message":"Register successfully",
        "Userdata": User
    }

@app.post("/pdf-reader")
async def create_upload_file(file: UploadFile = File(...)):
    filePath = os.path.join(uploadPath, file.filename)
    with open(filePath, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    with pdfplumber.open(filePath) as pdf:
        for page in pdf.pages:
            # print(pdf.pages)
            pagesData = page.extract_text()

    return {
        "filename": file.filename,
        "filepath": filePath,
        # "content_type": file.content_type,
        # "message":"File added successfully",
        # "Data": file,
        "fileData":pagesData
    }