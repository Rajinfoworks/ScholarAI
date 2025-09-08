from fastapi import APIRouter
from pydantic import BaseModel
import openai
from .upload import documents

openai.api_key = "YOUR_OPENAI_API_KEY"
router = APIRouter()

class Question(BaseModel):
    filename: str
    question: str

@router.post("/")
def ask_question(data: Question):
    if data.filename not in documents:
        return {"error": "File not found"}
    text = documents[data.filename]['text']
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": f"Based on this document:\n{text}\nAnswer: {data.question}"}
        ]
    )
    answer = response.choices[0].message.content
    return {"answer": answer}
