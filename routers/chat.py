from fastapi import  APIRouter
from pydantic import BaseModel

router=APIRouter()

class ChatRequest(BaseModel):
    question:str

class ChatResponse(BaseModel):
    answer:str

@router.post("/chat",response_model=ChatResponse)
def chat(request:ChatRequest):
    from services.rag_service import RAGService
    answer=RAGService().chat(request.question)
    return ChatResponse(answer=answer)