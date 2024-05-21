"""
Flag (Bandeira) - marcar um local 
None = Não valor
is e is not = é ou não é (tipo, valor, identidade)

id = Identidade
"""

condicao = True
passou_no_if = None

if condicao:
    passou_no_if = True
    print('Faça algo')
else:
    print('Não faça algo')

if passou_no_if is None:
    print('Não entrou no if')

if passou_no_if is not None:
    print('Entrou no if')

v1 = 'a'
v2 = 'a'
print(id(v1))
print(id(v2))