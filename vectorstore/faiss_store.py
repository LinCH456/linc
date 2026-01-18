import faiss
import numpy as np
import os
import json

class FaissVectorStore:
    """


    """
    def __init__(self,dim:int,index_path:str,meta_path:str):# 初始化向量数据库
        self.dim= dim# 向量维度
        self.index_path=index_path# 索引文件路径
        self.meta_path=meta_path# 元数据文件路径
        self.index=None# 索引 存储向量
        self.metadatas=[]# 元数据 存储元数据
        self._load()# 加载向量数据库

    # 加载向量数据库
    def _load(self):
        # 加载索引 存储向量
        if os.path.exists(self.index_path): # 判断索引文件是否存在
            self.index=faiss.read_index(self.index_path) # 加载索引
        else:
            self.index=faiss.IndexFlatL2(self.dim) # 创建一个空的索引 存储向量

        # 加载元数据
        if os.path.exists(self.meta_path): # 判断元数据文件是否存在
            with open(self.meta_path, 'r') as f:# 打开元数据文件
                self.metadatas=json.load(f)# 加载元数据 存储元数据
        else:
            self.metadatas=[]# 创建一个空列表

    # 保存向量数据库
    def _persist(self): # 保存向量数据库 仅提供内部使用的 方法
        faiss.write_index(self.index,self.index_path) # 保存索引
        with open(self.meta_path,"w",encoding="utf-8") as f:# 打开元数据文件
            json.dump(self.metadatas,f,ensure_ascii=False) # 保存元数据

    # 添加向量
    def add(self,vectors:np.ndarray,metadatas): # 添加向量
        self.index.add(vectors) # 添加向量
        self.metadatas.extend(metadatas) # 添加元数据
        self._persist() # 保存向量数据库
        print("向量数据库保存成功")

    # 搜索向量
    def search(self,query_vector:np.ndarray,top_k:int):
        if self.index.ntotal == 0: # 判断索引是否为空 ntotal 为索引中向量的数量(faiss内置函数)
            return []# 如果没有向量则返回空列表

        distances,indices=self.index.search(  #distances: 距离向量(numpy数组形式，返回top-k个最近向量）indices:索引向量(numpy数组形式，用以查找向量的位置索引）)
            query_vector.reshape(1,-1), # 将向量转换为矩阵 统一为1行多维的形式，-1表示自动匹配列数
            top_k

        )
        results=[]
        for idx in indices[0]:
            results.append(self.metadatas[idx]) # 将索引向量对应的元数据添加到结果列表中
        return  results

    # 删除向量
    def delete(self, index: int):
        # FAISS的remove_ids方法接受一个IDSelector对象
        # IDSelectorBatch用于删除一批ID
        id_selector = faiss.IDSelectorBatch(1, np.array([index], dtype=np.int64))
        self.index.remove_ids(id_selector)
        # 更新元数据列表，移除对应索引的数据
        if 0 <= index < len(self.metadatas):
            del self.metadatas[index]
        # 保存更新后的索引和元数据
        self._persist()
