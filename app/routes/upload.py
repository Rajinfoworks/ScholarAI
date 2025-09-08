from fastapi import APIRouter, UploadFile, File
from ..utils.pdf_parser import extract_text
from ..utils.embeddings import save_embeddings

router = APIRouter()
documents = {}

@router.post("/")
async def upload_pdf(file: UploadFile = File(...)):
    contents = await file.read()
    temp_file = f"temp_{file.filename}"
    with open(temp_file, "wb") as f:
        f.write(contents)
    text = extract_text(temp_file)
    embeddings = save_embeddings(text)
    documents[file.filename] = {"text": text, "embeddings": embeddings}
    return {"filename": file.filename, "status": "uploaded"}
