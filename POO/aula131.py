# @property - um getter no modo Pythônico
# getter - um método para obter um atributo
# modo Pythônico - modo do Python de fazer as coisas
# @property é uma propriedade do objeto, ela
# é um método que se comporta como um atributo
# Geralmente é usada nas seguintes situações:
# - como getter
# - p/ evitar quebrar o código cliente
# - p/ habilitar setter
# - p/ executar ações ao obter um atributo 
class Caneta:
    def __init__(self, cor):
        self.cor_tinta =  cor
    
    @property
    def cor(self):
        return self.cor_tinta
    
    @property
    def cor_tampa(self):
        return 123456
    
    # def get_cor(self):
    #     print('GET COR')
    #     return self.cor

caneta = Caneta('Azul')
print(caneta.cor)
print(caneta.cor_tampa)