"""
Iterável -> str, range, etc.
Iterator -> quem sabe entregar um valor por vez.
next -> me entregue o próximo valor.
iter -> me entregue seu iterador
""" 

texto = iter('Henrique') #iterável
iterator = iter(texto)

while True:
    try:
        print(next(iterator))
    except StopIteration:
        break