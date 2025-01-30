
from atividade1 import *
from atividade2 import *

calc = Calculadora()
div = DivisaoInt()
resto = RestoDivisao()
mult = Multiplicacao()

calc.adicionar_observador(div)
calc.adicionar_observador(resto)
calc.adicionar_observador(mult)
calc.set_valores(15, 3)
calc.set_valores(15, 4)
calc.set_valores(15, 0)
print(f"\n\n")

reuters = Reuters()
fox = FoxNews()
cnn = CNN()
globo = Globo()

reuters.inscrever(fox)
reuters.inscrever(cnn)
reuters.inscrever(globo)
reuters.nova_noticia("Dolar dispara!")
reuters.nova_noticia("Elon Musk irá salvar astronautas junto da Nasa!")