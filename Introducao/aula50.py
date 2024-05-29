"""
Exercicio
Exiba os índices da lista
"""

lista = ['Maria', 'Helena', 'Henrique']
lista.append('João')
indices = range(len(lista))

for indice in indices:
    print(lista[indice], type(lista[indice]), indice)