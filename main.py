from fastapi import FastAPI
from pydantic import BaseModel
from workflows.home_office import HomeOfficeWorkflow

app = FastAPI()

# --- Ask Endpoint (existing) ---
class Question(BaseModel):
    question: str

@app.post("/ask")
async def ask_question(q: Question):
    return {"answer": "You asked: " + q.question}


# --- Conversational Chat Endpoint ---
class Message(BaseModel):
    input: str

# In-memory workflow instance
workflow = HomeOfficeWorkflow()

@app.post("/chat/home-office")
async def chat_home_office(msg: Message):
    reply = workflow.next(msg.input)
    return {"response": reply}

