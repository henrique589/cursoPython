"""
Formatação básica de strings
s - string
d - int
f - float
.<número de dígitos>f
x ou X - Hexadecimal
> - Esquerda
< - Direita
^ - Centro
Conversion flags - !r !s !a
"""

variavel = 'ABC'
print(f'{variavel}')
print(f'{variavel: >10}')
print(f'{variavel:$^10}')
print(f'{1000.4834743490:0>+10,.1f}')