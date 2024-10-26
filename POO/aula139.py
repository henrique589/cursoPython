# super() é a super classe na subclasse 
# Classe principal (Pessoa)
#     -> super class, base class, parent class
# Classes filhas (Cliente)
#     -> sub class, child class, derived class
# class MinhaString(str):
    
#     def upper(self):
#         print('Chamou upper')
#         return super().upper()

# string = MinhaString('Henrique')
# print(string.upper())
class A:
    atributo_a = 'valor_a'

    def __init__(self, atributo):
        self.atributo = atributo

    def metodo(self):
        print('A')

class B(A):
    atributo_b = 'valor_b'

    def __init__(self, atributo, outra_coisa):
        super().__init__(atributo)
        self.outra_coisa = outra_coisa

    def metodo(self):
        print('B')

class C(B):
    atributo_c = 'valor_c'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def metodo(self):
        super().metodo()
        print('C')

c = C('atrinuto', 'ou')
print(c.atributo)
print(c.outra_coisa)
print(c.atributo_a)
print(c.atributo_b)
print(c.atributo_c)
c.metodo()