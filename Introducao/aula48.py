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

lista = [10, 20, 30, 40]
"""lista[2] = 300
del lista[2]
print(lista)
print(lista[2])"""
lista.append(50)
lista.pop()
lista.append(60)
lista.append(70)
ultimo_valor = lista.pop(3)
print(lista, 'Removido,', ultimo_valor)