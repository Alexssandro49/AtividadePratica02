# -*- coding: utf-8 -*-
from Desafio5 import *
from Desafio3 import *

print(f"Desafio-3 Sistema de Café\n\n")

cafe1 = Cafe()
print(f"Pedido: {cafe1.get_descricao()} - Preço: R${cafe1.get_preco():.2f}")

cafe2 = Cafe()
adicionar_leite(cafe2)
adicionar_canela(cafe2)
print(f"Pedido: {cafe2.get_descricao()} - Preço: R${cafe2.get_preco():.2f}")

cafe3 = Cafe()
adicionar_chocolate(cafe3)
adicionar_leite(cafe3)
print(f"Pedido: {cafe3.get_descricao()} - Preço: R${cafe3.get_preco():.2f}")

cafe4 = Cafe()
adicionar_leite(cafe4)
adicionar_chocolate(cafe4)
adicionar_canela(cafe4)
print(f"Pedido: {cafe4.get_descricao()} - Preço: R${cafe4.get_preco():.2f}")

print(f"\n\nDesafio-5 Logger com Níveis\n")

logger1 = log_com_nivel("INFO")(log_com_data(logger_base))
logger1("Sistema iniciado com sucesso.")


logger2 = log_em_arquivo("logs.txt")(log_com_nivel("WARNING")(log_com_data(logger_base)))
logger2("Memória acima de 80%.")


logger3 = log_em_arquivo("logs.txt")(log_com_nivel("ERROR")(log_com_data(logger_base)))
logger3("Erro crítico: conexão perdida!")

