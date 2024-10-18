# @property + @setter - getter e setter no modo Pythônico
# - p/ evitar quebrar o código cliente
# - p/ habilitar setter
# - p/ executar ações ao obter um atributo 
# Atributos que começam com um ou dois underlines 
# não devem ser usados fora da classe.
class Caneta:
    def __init__(self, cor):
        self._cor = cor
        self._cor_tampa = None
    
    @property
    def cor(self):
        return self._cor
    
    @cor.setter
    def cor(self, valor):
        if valor == 'Rosa':
            raise ValueError('Não aceito essa cor')
        self._cor = valor

    @property
    def cor_tampa(self):
        return self._cor_tampa
    
    @cor_tampa.setter
    def cor_tampa(self, valor):
        self._cor_tampa = valor

caneta = Caneta('Azul')
caneta.cor_tampa = 'Pink'
# caneta.cor = 'Rosa'
print(caneta.cor)
print(caneta.cor_tampa)
# getter -> obter valor