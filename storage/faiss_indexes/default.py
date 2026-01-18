import faiss
import os
import pickle
from typing import Optional

INDEX_PATH="storage/faiss_indexes/default.py"
DIMENSION=768

class FaissIndexManger:
    def __init__(self,dim:int=DIMENSION):
        self.dim=dim
        self.index=None

    def create_index(self):
        self.index=faiss.IndexFlatL2(self.dim)
        return self.index

    def load_index(self)->faiss.Index: # 加载索引
        """

        :return:
        """
        if not os.path.exists(INDEX_PATH):
            self.create_index()
            self.save_index()
        with open(INDEX_PATH,"rb") as f:
            self.index=pickle.load(f)
        return self.index

    def save_index(self): # 保存索引
        """
        持久化索引
        """
        if self.index is None:
            raise ValueError("FAISS index is None")

        faiss.write_index(self.index, INDEX_PATH)

    def add_vectors(self, vectors): # 添加向量
        """
        vectors: np.ndarray [n, dim]
        """
        if self.index is None:
            self.load_index()

        self.index.add(vectors)

    def search(self, query_vector, top_k=5): # 搜索
        """
        query_vector: np.ndarray [1, dim]
        """
        if self.index is None:
            self.load_index()

        distances, indices = self.index.search(query_vector, top_k)
        return distances, indices

    def get_index(self, index_name: str):
        """
        获取指定名称的索引
        :param index_name: 索引名称
        :return: FAISS索引对象
        """
        index_path = f"storage/faiss_indexes/{index_name}.index"
        
        if not os.path.exists(index_path):
            raise FileNotFoundError(f"Index file {index_path} does not exist")
            
        return faiss.read_index(index_path)
