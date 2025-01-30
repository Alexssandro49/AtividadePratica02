#encoding: latin-1
from abc import ABC, abstractmethod

class Operacao(ABC):
    @abstractmethod
    def update(self, valor1, valor2):
        pass

class DivisaoInt(Operacao):
    def update(self, valor1, valor2):
        if valor2 != 0:
            print(f"Divis�o inteira: {valor1} // {valor2} = {valor1 // valor2}")
        else:
            print("Erro! Divis�o por zero.")

class RestoDivisao(Operacao):
    def update(self, valor1, valor2):
        if valor2 != 0:
            print(f"Resto : {valor1} % {valor2} = {valor1 % valor2}")
        else:
            print("Erro! Divis�o por zero.")

class Multiplicacao(Operacao):
    def update(self, valor1, valor2):
        print(f"Multiplica��o: {valor1} * {valor2} = {valor1 * valor2}")


class Calculadora:
    def __init__(self):
        self._observadores = []
        self._valor1 = 0
        self._valor2 = 1

    def adicionar_observador(self, observador):
        self._observadores.append(observador)

    def remover_observador(self, observador):
        self._observadores.remove(observador)

    def set_valores(self, valor1, valor2):
        self._valor1 = valor1
        self._valor2 = valor2
        self._notificar()

    def _notificar(self):
        for obs in self._observadores:
            obs.update(self._valor1, self._valor2)




