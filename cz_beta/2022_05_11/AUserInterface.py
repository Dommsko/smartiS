from abc import ABC, abstractmethod
 
class AUserInterface(ABC):
 
    @abstractmethod
    def resize(self):
        pass
