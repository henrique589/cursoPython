"""
Closure e funções que retornam outras funções
"""

def criar_saudacao(saudacao):
    def saudar(nome):
        return f'{saudacao}, {nome}!'
    return saudar

s1 = criar_saudacao('Bom dia')
print(s1('Henrique'))

s2 = criar_saudacao('Boa noite')
print(s2('Henrique'))

for nome in ['Maria', 'Joana', 'Henrique']:
    print(s1(nome))
    print(s2(nome))