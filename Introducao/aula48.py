"""
Listas
Tipo list - Mutável
Suporta valores de qualquer tipo
índices e fatiamento
Métodos úteis: append, insert, pop, del, clear, extend, +
pop() remove o último item da lista
"""

# lista = list()

"""lista = [123, True, 'Henrique', 1.3, []]
lista[2] = 'João'
print(lista)
print(lista[2], type(lista[2]))"""


"""lista[2] = 300
del lista[2]
print(lista)
print(lista[2])
lista.append(50)
lista.pop()
lista.append(60)
lista.append(70)
ultimo_valor = lista.pop(3)
print(lista, 'Removido,', ultimo_valor)"""

"""
append - adiciona um item no final
insert - adiciona um item no índice escolhido
pop - remove do final ou do índice escolhido
del - apaga um índice
clear - limpa a lista
extend - estende a lista
+ - concatena a lista

"""

"""lista = [10, 20, 30, 40]
lista.append('Henrique')
nome = lista.pop()
lista.append(1233)
del lista[-1]
lista.insert(0, 5)
print(lista)"""

"""lista_a = [1, 2, 3]
lista_b = [4, 5, 6]
lista_c = lista_a + lista_b
lista_a.extend(lista_b)
print(lista_a)"""

lista_a = ['Henrique', 'Maria']
lista_b = lista_a.copy()
lista_a[0] = 'Qualquer coisa'
print(lista_b)