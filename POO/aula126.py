# __dict__ e vars para atributos de instância
class Pessoa:
    ano_atual = 2024

    def __init__(self, nome, idade):
        self.nome = nome,
        self.idade = idade

    def get_ano_nascimento(self):
        return Pessoa.ano_atual - self.idade

data = {'nome': 'Ana', 'idade': 23}
p3 = Pessoa(**data)
print(p3.nome)
    
p1 = Pessoa('Henrique', 21)
p2 = Pessoa('Ana', 23)

print(p1.get_ano_nascimento())
print(p2.get_ano_nascimento())

print(p1.__dict__)
print(vars(p2))

p1.__dict__['nome'] = 'teste'
print(p1.nome)