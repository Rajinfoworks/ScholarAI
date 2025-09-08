from fastapi import APIRouter, UploadFile, File
from ..utils.pdf_parser import summarize_text

router = APIRouter()

@router.post("/")
async def summarize_pdf(file: UploadFile = File(...)):
    contents = await file.read()
    temp_path = f"temp_{file.filename}"
    with open(temp_path, "wb") as f:
        f.write(contents)
    
    text = summarize_text(contents.decode("utf-8"))
    return {"filename": file.filename, "summary": text}
