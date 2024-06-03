"""
Introdução ao desempacotamento + tuples (tuplas)
"""

nome1, nome2, nome3 = ['Maria', 'Helena', 'Henrique']
print(nome2)

nome1, *_ = ['Maria', 'Helena', 'Henrique']
print(nome1, _)

_, nome2, *_ = ['Maria', 'Helena', 'Henrique']
print(nome2)