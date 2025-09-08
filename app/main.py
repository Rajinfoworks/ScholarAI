from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routes import upload, qa  # Only import what you have

app = FastAPI(title="ScholarAI MVP")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(upload.router, prefix="/upload")
app.include_router(qa.router, prefix="/qa")

@app.get("/")
def root():
    return {"message": "ScholarAI Backend Running"}
