#Operadores lógicos
"""
and -> verdadeiro se apenas as condições são todas verdadeiras.
"""

"""entrada = input('[E]ntrar [S]air: ')
senha_digitada = input('Senha: ')

senha_permitida = '123456'
if entrada == 'E' and  senha_digitada == senha_permitida:
    print('Entrar')
else:
    print('Sair')"""

# Avaliação de curto circuito
print(True and False and True)

if 1 and 1:
    print(True and 1 and False)