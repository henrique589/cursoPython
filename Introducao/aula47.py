"""
Faça um jogo para o usuário advinhar qual a palavra secreta.
- Você vai propor uma palavra secreta qualquer e vai dar a possibilidade
para o usuário digitar apenas uma letra.
- Quando o usuário digitar um letra, você vai conferir se a letra digitada
está na palavra secreta.
    - Se a letra digitada estiver na palavra secreta; exiba a letra;
    - Se a letra digitada não estiver na palavra secreta; exiba *.

Faça a contagem de tentativas do seu usuário.
"""
import os

palavra_secreta = 'perfume'
letras_acertadas = ''
tentativa = 0

while True:

    tentativa += 1
    letra_digitada = input('Digite uma letra: ')

    if(len(letra_digitada) != 1):
        continue

    if letra_digitada in palavra_secreta:
        letras_acertadas += letra_digitada

    palavra_advinha = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            palavra_advinha += letra_secreta
        else:
            palavra_advinha += '*'

    print('Palavra formada: ', palavra_advinha)

    if palavra_advinha == palavra_secreta:
        os.system('cls')
        print('VOCÊ GANHOU!')
        print('A palavra era: ', palavra_secreta)
        print('Tentativas: ', tentativa)
        letras_acertadas = ''
        tentativa = 0