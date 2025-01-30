from Caipirinhas import DrinkDecorator

class Saque(DrinkDecorator):
    def get_descricao(self):
        return self._drink.get_descricao() + ", Saqué"

    def get_preco(self):
        return self._drink.get_preco() + 5.0  


class Vodka(DrinkDecorator):
    def get_descricao(self):
        return self._drink.get_descricao() + ", Vodka"

    def get_preco(self):
        return self._drink.get_preco() + 6.0


class Abacaxi(DrinkDecorator):
    def get_descricao(self):
        return self._drink.get_descricao() + ", Abacaxi"

    def get_preco(self):
        return self._drink.get_preco() + 3.0


class Kiwi(DrinkDecorator):
    def get_descricao(self):
        return self._drink.get_descricao() + ", Kiwi"

    def get_preco(self):
        return self._drink.get_preco() + 4.0


class Morango(DrinkDecorator):
    def get_descricao(self):
        return self._drink.get_descricao() + ", Morango"

    def get_preco(self):
        return self._drink.get_preco() + 4.0


class Acucar(DrinkDecorator):
    def get_descricao(self):
        return self._drink.get_descricao() + ", Açucar"

    def get_preco(self):
        return self._drink.get_preco() + 1.0


class Adocante(DrinkDecorator):
    def get_descricao(self):
        return self._drink.get_descricao() + ", Adoçante"

    def get_preco(self):
        return self._drink.get_preco() + 1.5