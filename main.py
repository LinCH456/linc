from fastapi import FastAPI
import os
from openai import OpenAI

from routers import chat
from Embedding.openai_embed import OpenAIEmbedding
from vectorstore.faiss_store import FaissVectorStore
from services.rag_service import RAGService

app = FastAPI(title="RAG-API", description="A simple RAG API", version="0.1.0", openapi_tags=[
    {"name": "chat", "description": "Chat with the RAG API"},
])





# ===路径配置===
INDEX_PATH="storage/faiss_indexes/default.py"
META_PATH="storage/metadata/dafault.py"

os.makedirs("storage/faiss_indexes", exist_ok=True)
os.makedirs("storage/metadata", exist_ok=True)

 # ===初始化组件===
embedder=OpenAIEmbedding(api_key=os.environ.get("OPENAI_API_KEY"),
                           model="text-embedding-v4",
                           base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",

                           )
dim=len(embedder.embed("初始化"))

vector_store=FaissVectorStore

llm_client=OpenAIEmbedding(api_key=os.environ.get("OPENAI_API_KEY"),
                           model="qwen-max",
                           base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",

                           )

rag_service=RAGService(embedder,vector_store,llm_client)

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}

@app.get("/health")
async def health():
    return {"status": "ok"}

@app.get("/chat")
async def chat(question: str):
    return rag_service.chat(question)


app.include_router(chat.router)