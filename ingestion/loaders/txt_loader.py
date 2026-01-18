from ingestion.loaders.base import BaseLoader


class TxtLoader(BaseLoader):
    """"

    """
    # 加载txt文件
    def load(self, file_path: str):
        with open(file_path, "r") as f:
            text = f.read()

        # 按空格分段(简单非常实用)
        paragraphs = [
            p.strip() for p in text.split("\n\n") if p.strip()

        ]
        return paragraphs

    # 加载并分块
    def load_and_split(self, file_path: str, chunk_size: int = 512, chunk_overlap: int = 0):
        paragraphs = self.load(file_path)
        docs = []
        for paragraph in paragraphs:
            docs.extend(self.split_text(paragraph, chunk_size, chunk_overlap))
        return docs
