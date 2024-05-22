"""
Calculadora com while
"""

while True:
    numero_1 = input('Digite um número: ')
    numero_2 = input('Digite outro número: ')
    operador = input('Digite o operador (+-/*): ')
    numero_1_float = 0
    numero_2_float = 0

    try:
        numero_1_float = float(numero_1)
        numero_2_float = float(numero_2)
    except Exception as error:
        print(error)

    if operador == '+':
        print(f'{numero_1_float + numero_2_float}')
    elif operador == '-':
        print(f'{numero_1_float - numero_2_float}')
    elif operador == '/':
        print(f'{numero_1_float / numero_2_float}')
    elif operador == '*':
        print(f'{numero_1_float * numero_2_float}')
    else:
        print('Operador Inválido!!!')
    sair = input('Quer sair? [s]im: ').lower().startswith('s')

    if sair:
        break