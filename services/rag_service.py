import os

class RAGService:

    def __init__(
            self,
            embedder,
            vector_store,
            llm_client,
            top_k=3,
            min_context_len=50


                 ):
        self.embedder = embedder
        self.vector_store = vector_store
        self.llm_client = llm_client
        self.top_k = top_k
        self.min_context_len = min_context_len

        self.system_prompt=self._load_prompt("../prompts/system.txt")
        self.user_prompt=self._load_prompt("../prompts/rag_qa.txt")
        self.assistant_prompt=self._load_prompt("../prompts/refusal.txt")


    # 加载提示信息
    def _load_prompt(self,file_name):
        with open(os.path.join("prompts",file_name),"r") as f:
            return f.read()

    def chat(self,question:str) -> str:
        #1:向量化 query
        q_vec = self.embedder.embed(question)

        #2:搜索最相似的文档
        results=self.vector_store.search(q_vec,self.top_k)

        #3:兜底回答
        context_texts=[r["text"] for r in results if "text" in r]
        context="\n".join(context_texts)

        if len(context.strip()) < self.min_context_len:
            return  self.assistant_prompt

        # 4:构造prompt

        user_prompt=self.user_prompt.format(question=question,context=context)

        messages=[
            {"role":"system","content":self.system_prompt},
            {"role":"user","content":user_prompt}
        ]

        #5:调用LLM
        resp=self.llm_client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages,
            stream=False,
            temperature=0.7,
        )

        return resp.choices[0].message.content



