# Exercício - Salve sua classe em JSON
# Salve os dados da sua classe em JSON 
# e depois crie novamente as instâncias
# da classe com os dados salvos
# Faça em arquivos separados
import json
CAMINHO_ARQUIVO  = 'JSON/aula127.json'

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

# Para salvar determinadas informações em um JSON
# geralmente será utilizado um iterável. Por exemplo: uma lista,
# uma estrutura de dados que conterá várias pessoas. 

p1 = Pessoa('Henrique', 21)
p2 = Pessoa('Ana', 23)
p3 = Pessoa('Lucas', 22)

bd = [p1.__dict__, p2.__dict__, p3.__dict__]

def fazer_dump():
    with open(CAMINHO_ARQUIVO, 'w') as file:
        json.dump(bd, file, ensure_ascii=False, indent=2)

if __name__ == '__main__':
    fazer_dump()