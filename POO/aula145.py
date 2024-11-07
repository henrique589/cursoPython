# Criando Exceptions em Python Orientado a Objetos
# Para criar uma Exception em Python, você só 
# precisa herdar de alguma exceção da linguagem.
# A recomendação da doc é herdar de Exception.
# Criando exceções (comum colocar Error ao final)
# Levantando (raise) / Lançando (throw) exceções
# Relançando exceções
class MyError(Exception):
    ...
