# Classes são moldes para criar novos objetos 
# As classes geram novos objetos (instâncias) que
# podem ter seus próprios atributos e métodos.

class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

p1 = Pessoa('Henrique', 'Azevedo')
# p1.nome = 'Henrique'
# p1.sobrenome = 'Azevedo'
print(p1.nome)
print(p1.sobrenome)