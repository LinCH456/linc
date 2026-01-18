# storage/metadata/default.py

import os
import json
from typing import Dict, Any

META_PATH = "storage/metadata/default.json"

class MetadataStore:
    def __init__(self):
        self.data: Dict[str, Any] = {}
        self.load()

    def load(self):
        if os.path.exists(META_PATH):
            with open(META_PATH, "r", encoding="utf-8") as f:
                self.data = json.load(f)
        else:
            self.data = {}

    def save(self):
        os.makedirs(os.path.dirname(META_PATH), exist_ok=True)
        with open(META_PATH, "w", encoding="utf-8") as f:
            json.dump(self.data, f, ensure_ascii=False, indent=2)

    def add(
        self,
        vector_id: int,
        content: str,
        source: str,
        extra: dict = None
    ):
        self.data[str(vector_id)] = {
            "content": content,
            "source": source,
            "extra": extra or {}
        }

    def batch_add(self, records: Dict[int, dict]):
        for vid, record in records.items():
            self.data[str(vid)] = record

    def get(self, vector_id: int):
        return self.data.get(str(vector_id))
