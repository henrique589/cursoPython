"""
Valores padrão para parâmetros
Ao definir uma função, os parâmetros podem ter valores padrão.
Caso o valor não seja enviado para o parâmetro, o valor padrão
será usado.

Toda vez que um parâmetro tiver um valor padrão, todos os 
valores futuros terão que ter um valor padrão
"""

def soma(x, y, z=None):
    if z is not None:
        print(f'{x=} {y=} {z=}', x + y + z)
    else:
        print(f'{x=} {y=}', x + y)

soma(1, 2)
soma(3, 5)
soma(100, 200)
soma(7, 9, 0)
soma(x=7, z=0, y=9)
