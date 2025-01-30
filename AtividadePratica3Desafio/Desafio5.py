from datetime import datetime
from functools import wraps

def logger_base(mensagem):
    print(mensagem)

def log_com_data(func):
    @wraps(func)
    def wrapper(mensagem):
        mensagem = f"{datetime.now().strftime('%d-%m-%y %H:%M:%S')} - {mensagem}"
        func(mensagem)
    return wrapper

def log_com_nivel(nivel):
    def decorador(func):
        @wraps(func)
        def wrapper(mensagem):
            mensagem = f"[{nivel}] {mensagem}"
            func(mensagem)
        return wrapper
    return decorador

def log_em_arquivo(nome_arquivo="log.txt"):
    def decorador(func):
        @wraps(func)
        def wrapper(mensagem):
            func(mensagem)  # Imprime no console
            with open(nome_arquivo, "a", encoding="utf-8") as f:
                f.write(mensagem + "\n")  # Salva no arquivo
        return wrapper
    return decorador