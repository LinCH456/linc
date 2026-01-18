from pypdf import PdfReader
from ingestion.loaders.base import BaseLoader


class PdfLoader(BaseLoader):

    def load(self, file_path: str):
        reader = PdfReader(file_path)
        texts = []
        for page in reader.pages:
            texts.append(page.extract_text())

        return texts

