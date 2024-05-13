nome = 'Henrique Azevedo'
altura = 1.85
peso = 75
imc = peso / altura**2


"f-strings"
linha_1 = f'{nome} tem {altura:.2f} de altura,' #utilizar 'f' habilita o uso de 
linha_2 = f'pesa {peso} quilos e seu imc é'     #variáveis em strings.
linha_3 = f'{imc:.2f}'
print(linha_1)                              
print(linha_2)
print(linha_3)