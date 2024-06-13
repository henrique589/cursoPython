# Exercício
# Crie funções que duplicam, triplicam e quadruplicam
# o número recebido como parâmetro.

def cria_multiplos(numero):
    def multiplicar(multiplo):
        return numero * multiplo
    return multiplicar

num_1 = cria_multiplos(3)
num_2 = cria_multiplos(5)
num_3 = cria_multiplos(7)

print(num_1(2))
print(num_2(3))
print(num_3(4))