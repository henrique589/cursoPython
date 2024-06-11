"""
Escopo de funções em Python
Escopo significa o local onde aquele código pode atingir.
Existe escopo global e local.
O escopo global é o escopo onde todo código é alcançável.
O escopo local é onde o escopo onde apenas os nomes do mesmo local
podem ser alcançados.
Não temos acesso a nomes de escopos internos nos escopos externos.
A palavra global faz uma variável do escopo externo ser a mesma
no escopo interno.
"""
x = 1

def escopo():
    global  x
    x = 2
    print(x)

print(x)
escopo()
print(x)