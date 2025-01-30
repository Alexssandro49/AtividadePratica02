# -*- coding: utf-8 -*-
from Ingredientes import *
from Caipirinhas import *


if __name__ == "__main__":
    drink1 = Acucar(Kiwi(Abacaxi(Saque(Caipira()))))
    print(f"Pedido: {drink1.get_descricao()} - Preço: R${drink1.get_preco():.2f}")

    drink2 = Adocante(Morango(Vodka(Caipira())))
    print(f"Pedido: {drink2.get_descricao()} - Preço: R${drink2.get_preco():.2f}")

    drink3 = CaipirinhaPadrao()
    print(f"Pedido: {drink3.get_descricao()} - Preço: R${drink3.get_preco():.2f}")