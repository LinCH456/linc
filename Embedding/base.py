from abc import  ABC ,abstractmethod
import  numpy as np


class BaseEmbedding(ABC):
    @abstractmethod
    def __init__(self):
        pass
    @abstractmethod
    def embed(self,text:str) -> np.ndarray:
        pass
