"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.

numero = input('Digite um número inteiro: ')
try:    
    numero_int = float(numero)
    if(numero_int % 2 == 0):
        print(f'O número {numero_int} é par!')
    else:
        print(f'O número {numero_int} é ímpar!')
except:
    print('Não digitou um número inteiro')
"""

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.


entrada_horario = input('Digite a hora para a saudação: ')

try:
    hora = int(entrada_horario)
    if(hora >= 0 and hora <= 11):
        print('Bom dia!')
    elif(hora >= 12 and hora <= 17):
        print('Boa tarde!')
    elif(hora >= 18 and hora <= 23):
        print('Boa noite!')
    else:
        print('Hora desconhecida!')
except:
    print('Não digitou um valor válido!')
"""

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

entrada_nome = input('Digite seu primeiro nome: ')
tam_nome = len(entrada_nome)

if (tam_nome <= 4):
    print('"Seu nome é curto"')
elif (tam_nome >= 5 and tam_nome <= 6):
    print('"Seu nome é normal"')
else:
    print('"Seu nome é muito grande"')