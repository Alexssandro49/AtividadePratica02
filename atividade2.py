#encoding: latin-1
from abc import ABC, abstractmethod

class CanalNoticia(ABC):
    @abstractmethod
    def update(self, noticia):
        pass

class FoxNews(CanalNoticia):
    def update(self, noticia):
        print(f"Fox News: {noticia}")

class CNN(CanalNoticia):
    def update(self, noticia):
        print(f"CNN: {noticia}")

class Globo(CanalNoticia):
    def update(self, noticia):
        print(f"Globo: {noticia}")

class Reuters:
    def __init__(self):
        self._canais = []
        self._ultima_noticia = None

    def inscrever(self, canal):
        self._canais.append(canal)

    def desinscrever(self, canal):
        self._canais.remove(canal)

    def nova_noticia(self, noticia):
        self._ultima_noticia = noticia
        self._notificar()

    def _notificar(self):
        for canal in self._canais:
            canal.update(self._ultima_noticia)




