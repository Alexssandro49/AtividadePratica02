from Interface import  * 

class Caipira(Drink):
    def get_descricao(self):
        return "Caipira"

    def get_preco(self):
        return 20.0

class CaipirinhaPadrao(Drink):
    def get_descricao(self):
        return "Caipirinha (Cachaça, Limão, Gelo e Açucar)"

    def get_preco(self):
        return 25.0 

class DrinkDecorator(Drink):
    def __init__(self, drink):
        self._drink = drink

    def get_descricao(self):
        return self._drink.get_descricao()

    def get_preco(self):
        return self._drink.get_preco()

