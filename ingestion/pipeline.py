import  os
import  numpy as np

class IngestionPipeline:
    """
    数据处理管道
    """
    def __init__(self,loader,chunker,embedder,vector_store):
        self.loader=loader
        self.chunker=chunker
        self.embedder=embedder
        self.vector_store=vector_store

    def ingest(self,file_path:str):
        # 1:读取文档
        texts=self.loader.load(file_path)
        # 2:分块处理
        chunk=self.chunker.chunk(texts)
        # 3:生成向量
        vectors=np.vstack(
            [self.embedder.embed(chunk) for chunk in chunk]
        )
        # 4:生成元数据
        metadatas=[
            {
                "text":chunk,
                "source":os.path.basename(file_path)
            }
        ]
        # 5:存储向量
        self.vector_store.add(vectors)
