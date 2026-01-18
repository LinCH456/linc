from   rank_bm25 import BM25Okapi
import jieba

class BM25Retriever:
    """
    BM25检索器

    """
    def __init__(self,documents):
        """
         docnments:List[str]
        :param documents:
        """
        self.documents=documents # 文档列表
        self.tokenized_docs=[list(jieba.cut(d)) for d in documents] # 分词 jieba: 分词
        self.bm25=BM25Okapi(self.tokenized_docs)

    def search(self,query:str,top_n:int=5 ):
        tokenized_query=list(jieba.cut(query))
        scores=self.bm25.get_scores(tokenized_query)

        ranked=sorted(
            enumerate(scores),
            key=lambda x:x[1],
            reverse=True

        )
        return ranked[:top_n]

from storage.metadata.dafault import MetadataStore

def build_bm25_corpus():
    metadata_store=MetadataStore()
    documents=[]
    id_map=[]

    for vid,record in metadata_store.items():
        documents.append(record["text"])
        id_map.append(vid)
    return documents,id_map