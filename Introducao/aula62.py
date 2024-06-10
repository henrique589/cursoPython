"""
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF mais o primeiro dígito
multiplicando cada um dos valores por uma contageem regressiva
começando de 10
"""
import re
import sys

"""cpf = '746.824.890-70' \
    .replace('.', '') \
    .replace(' ', '') \
    .replace('-', '')"""
entrada = input('CFP: [746.824.890-70] ')

cpf = re.sub(
    r'[^0-9]',
    '',
    entrada
    )

entrada_e_sequencial = entrada == entrada[0] * len(entrada)

if entrada_e_sequencial:
    print('Você enviou dados sequenciais')
    sys.exit()

cpf_9_digitos = cpf[0:9]
contador_1 = 10
resultado_1 = 0

for digito in cpf_9_digitos:
    resultado_1 += int(digito) * contador_1
    contador_1 -= 1

digito_1 = (resultado_1 * 10) % 11
digito_1 = digito_1 if digito_1 <= 9 else 0

cpf_10_digitos = cpf_9_digitos + str(digito_1)
contador_2 = 11
resultado_2 = 0

for digito in cpf_10_digitos:
    resultado_2 += int(digito) * contador_2
    contador_2 -= 1

digito_2 = (resultado_2 * 10) % 11
digito_2 = digito_2 if digito_2 <= 9 else 0

novo_cpf = f'{cpf_9_digitos}{digito_1}{digito_2}'
if cpf == novo_cpf:
    print(f'{cpf} é válido')
else:
    print('CPF inválido')