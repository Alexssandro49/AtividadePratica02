#encoding: latin-1
from Interface import  * 

class Caipira(Drink):
    def get_descricao(self):
        return "Caipira"

    def get_preco(self):
        return 20.0

class CaipirinhaPadrao(Drink):
    def get_descricao(self):
        return "Caipirinha (Cacha�a, Lim�o, Gelo e A��car)"

    def get_preco(self):
        return 25.0  # Pre�o fixo

class DrinkDecorator(Drink):
    def __init__(self, drink):
        self._drink = drink

    def get_descricao(self):
        return self._drink.get_descricao()

    def get_preco(self):
        return self._drink.get_preco()

