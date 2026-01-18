from Embedding.openai_embed import OpenAIEmbedding
from vectorstore.faiss_store import FaissVectorStore
import numpy as np
import os

embedder = OpenAIEmbedding(api_key="sk-7b080ec258704e5794529f7f2ab00b93 ",
                           model="text-embedding-v4",
                           base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",

                           )

docs = [
    "员工每天9点前必须打卡",
    "迟到超过30分钟视为旷工",
    "公司实行双休制度",
    "员工每天下午4点30左右必须打卡",
    "员工每天下午5点30左右必须打卡",
    "员工每天下午6点左右必须打卡",
    "员工每天下午7点左右必须打卡",
]

vectors=np.vstack([embedder.embed(doc) for doc in docs]) # 生成向量

store=FaissVectorStore(dim=vectors.shape[1])
# 添加向量
store.add(
    vectors,
    [{"text": doc} for doc in docs]

)

query=" 迟到会怎么样"
q_vec=embedder.embed(query)

results=store.search(q_vec,top_k=3)
print(results)


