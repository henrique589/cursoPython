"""
Introdução as funções (def) em Python
Funções são trechos de código usados para
replicar determinada ação ao longo do seu código.
Elas podem receber valores para parâmetros (argumentos)
e retornar um valor específico.
Por padrão, funções em Python retornam None (nada).

Parâmetro é a variável no cabeçalho da função
Argumento é a passagem dos valores na chamada da função
"""
def Print(a, b, c):
    print('Várias')
    print('Várias')
    print('Várias', 'Vezes')

def imprimir(a, b, c):
    print(a, b, c)

def saudacao(nome='Sem nome'):
    print(f'Olá, {nome}!')

nome = input('Digite seu nome: ')
saudacao(nome)
saudacao()
#imprimir(1, 2, 3)
#imprimir(4, 5, 6)