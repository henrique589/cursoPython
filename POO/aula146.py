# Criando Exceptions em Python Orientado a Objetos
# Para criar uma Exception em Python, você só 
# precisa herdar de alguma exceção da linguagem.
# A recomendação da doc é herdar de Exception.
# Criando exceções (comum colocar Error ao final)
# Levantando (raise) / Lançando (throw) exceções
# Relançando exceções
class MyError(Exception):
    ...

class AnotherError(Exception):
    ...

def levantar():
    exception_ = MyError('a', 'b', 'c')
    exception_.add_note('Olha a nota 1')
    exception_.add_note('Algo de errado')
    raise exception_

try:
    levantar()
except (MyError, ZeroDivisionError) as error:
    print(error.__class__.__name__)
    print(error)
    print()
    exception_ = AnotherError('Vou lançar novamente')
    exception_.add_note('Mais uma nota')
    exception_.__notes__ += error.__notes__.copy()
    raise exception_ from error