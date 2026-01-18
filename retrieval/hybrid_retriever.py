import numpy as np
from storage.faiss_indexes.default import FaissIndexManger
from storage.metadata.dafault import MetadataStore

class VectorRetriever:
    def __init__(self):
        self.index_manage=FaissIndexManger() # 索引管理
        self.index=self.index_manage.get_index() # 获取索引