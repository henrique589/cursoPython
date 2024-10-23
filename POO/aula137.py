# Exercícios com classes
# 1 - Crie uma classe Carro (Nome)
# 2 - Crie uma classe Motor (Nome)
# 3 - Crie uma classe Fabricante (Nome)
# 4 - Façaa ligação entre carro e motor
# Obs: Um motor pode ser de vários carros
# 5 - Faça a ligação entre Carro e Fabricante
# Obs: Um fabricante pode fabricas vários carros
# Exiba o nome do carro,  motor e fabricantes na tela
class Carro:
    def __init__(self, nome):
        self.nome = nome
        self._motor = None
        self._fabricante = None
    
    @property
    def motor(self):
        return self._motor
    
    @motor.setter
    def motor(self, motor):
        self._motor = motor

    @property
    def fabricante(self):
        return self._fabricante
    
    @fabricante.setter
    def fabricante(self, fabricante):
        self._fabricante = fabricante

class Motor:
    def __init__(self, nome):
        self.nome = nome

class Fabricante:
    def __init__(self, nome):
        self.nome = nome

fusca = Carro('Fusca')
fusca.fabricante = Fabricante('Volkswagen')
fusca.motor = Motor('1.0')
print(fusca.nome, fusca.fabricante.nome, fusca.motor.nome)