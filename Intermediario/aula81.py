# Função lambda em Python
# A função lambda é uma função como qualquer 
# outra em Python. Porém, são funções anônimas 
# que contém apenas uma linha. Ou seja, tudo 
# dever ser contido dentro de uma única 
# expressão

# lista = [
#     {'nome': 'Luiz', 'sobrenome': 'miranda'},
#     {'nome': 'Maria', 'sobrenome': 'Oliveira'},
#     {'nome': 'Daniel', 'sobrenome': 'Silva'},
#     {'nome': 'Eduardo', 'sobrenome': 'Moreira'},
#     {'nome': 'Aline', 'sobrenome': 'Souza'},
# ]

# lista = [1, 2, 3, 5, 32, 2]
# lista.sort(reverse=True)

lista = [
    {'nome': 'Luiz', 'sobrenome': 'miranda'},
    {'nome': 'Maria', 'sobrenome': 'Oliveira'},
    {'nome': 'Daniel', 'sobrenome': 'Silva'},
    {'nome': 'Eduardo', 'sobrenome': 'Moreira'},
    {'nome': 'Aline', 'sobrenome': 'Souza'},
]

# def ordena(item):
#     return item['nome']

# lista.sort(key=ordena)

# for item in lista:
#     print(item)

def exibir(lista):
    for item in lista:
        print(item)

# lista.sort(key=lambda item: item['sobrenome'])
l1 = sorted(lista, key=lambda item: item['nome'])
l2 = sorted(lista, key=lambda item: item['sobrenome'])

exibir(l1)
exibir(l2)