from functools import wraps

# 🎯 Classe base para o café
class Cafe:
    def __init__(self):
        self.descricao = "Café Simples"
        self.preco = 5.0  # Preço base do café

    def get_descricao(self):
        return self.descricao

    def get_preco(self):
        return self.preco

# ☕ Decorador para adicionar ingredientes extras
def adicionar_ingrediente(nome, custo):
    def decorador(func):
        @wraps(func)
        def wrapper(cafe):
            cafe.descricao += f", {nome}"  # Adiciona o nome do ingrediente
            cafe.preco += custo  # Adiciona o custo do ingrediente
            func(cafe)  # Chama a função original
        return wrapper
    return decorador

# 🥛 Leite Vaporizado (+2.0)
@adicionar_ingrediente("Leite Vaporizado", 2.0)
def adicionar_leite(cafe):
    pass

# 🍫 Chocolate (+3.0)
@adicionar_ingrediente("Chocolate", 3.0)
def adicionar_chocolate(cafe):
    pass

# 🍂 Canela (+1.5)
@adicionar_ingrediente("Canela", 1.5)
def adicionar_canela(cafe):
    pass