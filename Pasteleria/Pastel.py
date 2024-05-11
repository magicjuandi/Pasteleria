from abc import ABC,abstractmethod

class Pastel(ABC):
    @abstractmethod
    def preparar(self):
        pass
    
    @abstractmethod
    def hornear(self):
        pass
    
    @abstractmethod
    def decorar(self):
        pass
    
    @abstractmethod
    def empacar(self):
        pass

