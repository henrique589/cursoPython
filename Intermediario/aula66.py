"""
Argumentos nomeados e não nomeados em funções Python
Argumento nomeado tem nome com sinal de igual
Argumento não nomeado recebe apenas o argumento (valor)
A partir de uma passagem de argumento nomeado, todos os outros
argumentos futuros devem ser passados da mesma maneira
"""

def soma(x, y, z):
    print(f'{x=} {y=} {z=}', '|', 'x+y+z= ', x + y + z)

soma(1, 2, 3)
soma(2, 1, 3)
soma(y=2, z=3, x=1)
soma(1, 2, z=5)