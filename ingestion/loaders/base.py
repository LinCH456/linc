from abc import ABC,abstractmethod
from typing import List

class BaseLoader(ABC):
    """
    数据加载器
    """
    @abstractmethod
    def load(self,file_path:str)->List[str]:
        """
        加载数据
        :param file_path: 文件路径
        :return: 数据列表
        返回文档的"原始文本段落列表"
        """
        pass

    @abstractmethod
    def load_and_split(self,file_path:str,chunk_size:int=1000,chunk_overlap:int=0)->List[str]:
        """
        加载并分块数据
        :param file_path: 文件路径
        :param chunk_size: 分块大小
        :param chunk_overlap: 分块重叠大小
        :return: 数据列表
        返回文档的"分块文本段落列表"
        """
        pass

