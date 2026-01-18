import numpy as np
from openai import OpenAI
from Embedding.base import BaseEmbedding


# OpenAIEmbedding  class
class OpenAIEmbedding(BaseEmbedding):
    def __init__(self,api_key:str,model:str,base_url:str):
        self.client=OpenAI(api_key=api_key,base_url=base_url)
        self.model=model

# embedding function
    def embed(self,text:str)->np.ndarray:
        resp=self.client.embeddings.create(
            model=self.model,
            input=text
        )
        return np.array(resp.data[0].embedding,dtype=np.float32)



