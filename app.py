from fastapi import FastAPI
from pydantic import BaseModel

from services.recommendation_service import process_chat


app = FastAPI()


class Message(BaseModel):
    role: str
    content: str


class ChatRequest(BaseModel):
    messages: list[Message]


@app.get("/health")
def health():
    return {
        "status": "ok"
    }


@app.post("/chat")
def chat(request: ChatRequest):

    messages = [
        message.model_dump()
        for message in request.messages
    ]

    return process_chat(messages)