"""
enumerate - enumera iteráveis (índices)
"""

lista = ['Maria', 'Helena', 'Henrique']
lista.append('João')

#lista_enumerada = list(enumerate(lista))

for indice, nome in enumerate(lista):
    print(indice, nome)
