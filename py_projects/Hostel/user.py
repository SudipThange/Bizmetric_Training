from abc import abstractmethod, ABC

class User(ABC):
    @abstractmethod
    def register(self):
        pass
    
    @abstractmethod
    def login(self):
        pass
    
    @abstractmethod
    def logout(self):
        pass


