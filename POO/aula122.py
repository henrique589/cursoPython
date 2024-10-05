# Entendendo self em classes Python

class Carro:
    def __init__(self, nome):
        self.nome = nome

    def acelerar(self):
        print(f'{self.nome} está acelerando...')

fusca = Carro('Fusca')
print(fusca.nome)
Carro.acelerar(fusca)
#fusca.acelerar()

celta = Carro('Celta')
print(celta.nome)
celta.acelerar()