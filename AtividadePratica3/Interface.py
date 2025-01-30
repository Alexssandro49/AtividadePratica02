from abc import ABC, abstractmethod

class Drink(ABC):
    @abstractmethod
    def get_descricao(self):
        pass

    @abstractmethod
    def get_preco(self):
        pass