nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')
encontrar = ' '

# if nome and idade:
# caso nada seja digitado será atribuído um valor falsi
if not nome and not idade:
    print('"Desculpe, você deixou os campos vazios."')
else:
    print(f'Seu nome é {nome}')
    print(f'Seu nome invertido é {nome[::-1]}')
    if encontrar in nome:
        print('O nome contém espaços.')
    else:
        print('O nome não contém espaços.')
    print(f'Seu nome tem {len(nome)} letras')
    print(f'A primeira letra do seu nome é {nome[0]}')
    print(f'A última letra do seu nome é {nome[-1]}')