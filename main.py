from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Question(BaseModel):
    question: str

@app.post("/ask")
async def ask_question(q: Question):
    return {"answer": "You asked: " + q.question}
