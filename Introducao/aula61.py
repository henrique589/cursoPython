"""
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma contageem regressiva
começando de 10
"""

cpf = '74682489070'
cpf_9_digitos = cpf[0:9]
contador_1 = 10
resultado_1 = 0

for digito_1 in cpf_9_digitos:
    resultado_1 += int(digito_1) * contador_1
    contador_1 -= 1

digito_1 = (resultado_1 * 10) % 11
digito_1 = digito_1 if digito_1 <= 9 else 0
print(digito_1)