# Exercícios com funções

# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável.

def multiplica(*args):
    total = 1
    for num in args:
        total *= num
    return total


total = multiplica(1, 2, 3, 4, 5, 6, 7)
print(total)

# Crie uma função que fala se um número é par ou ímpar.
# Retorne se o número é par ou ímpar.

def par(num):
    if num % 2 == 0:
        return True
    else:
        return False
    
numero = par(16)
if numero == True:
    print('O número é par')
else:
    print('O número é ímpar')