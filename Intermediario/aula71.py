"""
args - argumentos não nomeados
* - *args (empacotamento e desempacotamento)
"""
# Lembre-se de desempacotamento
x, y, *resto = 1, 2, 3, 4
print(x, y, resto, type(x))

#def soma(x, y):
#    return x + y

def soma(*args):
    total = 0
    for numero in args:
        total += numero
    return total

numeros = 1, 2, 3, 4, 5, 6
variavel = soma(*numeros)