# Herança múltipla - Python Orientado a Objetos
# Quer dizer que no Python, uma classe pode estender
# várias outras classes.
# Herança simples:
# Animal -> Mamífero -> Humano -> Pessoa -> Cliente
# Herança múltipla e mixins
# Log -> Filelog
# Animal -> Mamífero -> Humano -> Pessoa -> Cliente
# Cliente(Pessoa, Filelog)

# Classe.mro()
# __mro__

class A:
    pass

    def quem_sou(self):
        print('A')

class B(A):
    pass

    # def quem_sou(self):
    #     print('B')

class C(A):
    pass

    def quem_sou(self):
        print('C')

class D(B, C):
    pass

    # def quem_sou(self):
    #     print('D')

d = D()
d.quem_sou()
print(D.__mro__)