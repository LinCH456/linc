import os
import numpy as np

from Embedding.openai_embed import OpenAIEmbedding
from vectorstore.faiss_store import FaissVectorStore
from ingestion.loaders.txt_loader import TxtLoader
from ingestion.loaders.pdf_loader import PdfLoader
from ingestion.chuking.fixed_chunk import FixedChunker
from ingestion.pipeline import  IngestionPipeline

embedder=OpenAIEmbedding(api_key="sk-7b080ec258704e5794529f7f2ab00b93 ",
                        model="text-embedding-v4",
                        base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",

                        )
#初始化向量库
dim=len(embedder.embed("测试"))
store=FaissVectorStore(dim=dim)
chunk=FixedChunker(chunk_size=300,overlap=50)

#初始化管道 Txt
txt_pipeline=IngestionPipeline(
    loader=TxtLoader(),
    chunker=chunk,
    embedder=embedder,
    vector_store=store
)
txt_pipeline.ingest("data/test.txt")

#Pdf
pdf_pipeline=IngestionPipeline(
    loader=PdfLoader(),
    chunker=chunk,
    embedder=embedder,
    vector_store=store

)

pdf_pipeline.ingest("data/test.pdf")

# 检索测试
query = "迟到怎么处理"
q_vec = embedder.embed(query)
results = store.search(q_vec, top_k=3)

for r in results:
    print(r)