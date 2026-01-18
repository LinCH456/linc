class FixedChunker:
    """
    固定分块器
    """
    def __init__(self,chunk_size=500,overlap=100):
        self.overlap=overlap
        self.chunk_size=chunk_size

    def chunk(self,text:str):
        chunks=[]
        for text in text.split("\n"):
            start=0
            length=len(text)

            while start<length:
                end=start+self.chunk_size
                chunk=text[start:end]
                chunks.append(chunk)
                start=end - self.overlap
        return chunks
