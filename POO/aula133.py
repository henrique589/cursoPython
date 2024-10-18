# Encapsulamento (modificadores de acesso: public, protected e private)
# Python não tem modificadores de acesso
# Mas podemos seguir as convenções
#     (sem underline) = public
#         pode ser usado em qualquer lugar
#     (um underline) = protected
#         não deve ser usado fora da classe
#         ou suas subclasses
#     (dois underlines) = private
#         "name mangling" (desconfiguração de nomes) em Python
#         só deve ser usado na classe em que foi declarado
class Foo:
    def __init__(self):
        self.public = 'isso é público'
        self._protected = 'isso é protegido'
        self.__private = 'isso é privado'
    
    def metodo_publico(self):
        print(self.__metodo_private())
        return 'metodo_publico'
    
    def _metodo_protected(self):
        return '_metodo_protected'
    
    def __metodo_private(self):
        return '__metodo_private'

f = Foo()
# print(f.public)
print(f.metodo_publico())