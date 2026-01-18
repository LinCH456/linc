from abc import  ABC ,abstractmethod
from typing import List


class BaseChunker(ABC):

    @abstractmethod
    def chunk(self,text:List[str])->List[str]:
        """
        分块
        :param text: 文本列表
        :return: 分块后的文本列表
        """
        pass
