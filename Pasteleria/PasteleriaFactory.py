from abc import ABC, abstractmethod

class PasteleriaFactory(ABC):
    @abstractmethod
    def crear_pastel(self):
        pass