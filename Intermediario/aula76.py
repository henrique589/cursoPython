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

pessoa = {}
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
    print(pessoa['sobrenome'])