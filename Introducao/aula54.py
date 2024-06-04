"""
Faça uma lista de compras com listas
O usuário deve ter a possibilidade de 
inserir, apagar e listar os valores da sua lista
Não permita que o programa quebre com índices inexistentes
na lista.
"""

lista_compras = []
opcao = ''
item = ''

while True:
    print('Seleciona uma opção')
    opcao = input('[i]nserir [a]pagar [l]istar: ')
    if opcao == 'i':
        item = input('Valor: ')
        lista_compras.append(item)
    elif opcao == 'a':
        indice = input('Escolha um índice para apagar: ')
        if (int(indice) < len(lista_compras)) or len(lista_compras) != 0:
            lista_compras.pop(int(indice))
        else:
            print('Não foi possível apagar este índice.')
    elif opcao == 'l':
        if lista_compras:
            for indice, valor in enumerate(lista_compras):
                print(indice, valor)
        else:
            print('Nada para listar.')
    else: 
        print('Comando desconhecido.')