# Dicionário em Python (tipo dict)
# Dicionários são estruturas de dados do tipo
# par de "chave" e "valor".
# Chaves podem ser consideradas como "índice"
# que vimos na lista e podem ser de tipos imutáveis
# como: str, int, floaat, bool, tuple, etc.
# O valor pode ser de qualquer tipo, incluindo outro dicionário.
# Usamos as chaves - {} - ou a classe dict para criar 
# dicionários.
# Imutáveis: str, int, float, boll, tuple
# Mutável: dict, list
"""pessoa = {
    'nome': 'Henrique',
    'sobrenome': 'Azevedo',
    'idade': 21,
    'altura': 1.85,
    'enderecos': [
        {'rua': 'tal qual', 'numero': 123},
        {'rua': 'outra rua', 'numero': 321},
    ]
}

print(pessoa, type(pessoa))
print(pessoa['nome'])

for chave in pessoa:
    print(chave, pessoa[chave])"""

## 
##

# Manioulando chaves e valores em dicionários

"""pessoa = {}
chave = 'nome_completo'
pessoa[chave] = 'Henrique'
pessoa['sobrenome'] = 'Azevedo'
print(pessoa)

print(pessoa[chave])
pessoa[chave] = 'Ana'
#del pessoa['sobrenome']
print(pessoa) 

if pessoa.get('sobrenome') is None:
    print('NÃO EXISTE')
else:
    print(pessoa['sobrenome'])"""

# Métodos úteis dos dicionários em Python
# len - quantas chaves
# keys - iterável com as chaves
# values - iterável com os valores
# items - iterável com chaves e valores
# setdefault - adiciona valor se a chave não existe
# copy - retorna uma cópia rasa (shallow copy)
# get - obtém uma chave
# pop - Apaga um item com a chave especificada (del)
# popitem - Apaga o último item adicionado
# update - Atualiza um dicionário com outro

"""pessoa = {
    'nome': 'Henrique',
    'sobrenome': 'Azevedo',
}"""

# print(tuple(pessoa.keys()))
# print(pessoa.values())
# print(list(pessoa.items()))

# for chave, valor in pessoa.items():
#    print(chave, valor)
# pessoa.setdefault('idade', 0)
# print(pessoa['idade'])
# import copy
"""
d1 = {
    'c1': 1,
    'c2': 2,
    'l1': [0, 1, 2],
}

d2 = copy.deepcopy(d1)
#d2 = d1.copy()

d2['c1'] = 1000
d2['l1'][1] = 9999
print(d1)
print(d2)"""

p1 = {
    'nome': 'Henrique',
    'sobrenome': 'Azevedo',
}
#print(p1.get('nome', 'Não existe'))
"""nome  = p1.pop('nome')
print(nome, p1)"""
# ultima_chave = p1.popitem()
# print(ultima_chave)
# print(p1)

p1.update({
    'nome': 'Ana',
    'idade': 22
})
print(p1)