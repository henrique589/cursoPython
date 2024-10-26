# Herança simples - Relações entre classes
# Associação - usa, Agregação - tem
# Composição - É dono de, Herança - É um

# Herança ou Composição

# Classe principal (Pessoa)
#     -> super class, base class, parent class
# Classes filhas (Cliente)
#     -> sub class, child class, derived class
class Pessoa:
    cpf = '123'

    def __init__(self, nome, sobrenome):
        self._nome = nome
        self._sobrenome = sobrenome

    def falar_nome_class(self):
        print('Pessoa')
        print(self._nome, self._sobrenome, self.__class__.__name__)

class Cliente(Pessoa):
    def falar_nome_class(self):
        print('Cliente')
        print(self._nome, self._sobrenome, self.__class__.__name__)
    
class Aluno(Pessoa):
    cpf = '12'

c1 = Cliente('Henrique', 'Azevedo')
a1 = Aluno('Ana', 'Laura')
c1.falar_nome_class()
a1.falar_nome_class()
print(a1.cpf)