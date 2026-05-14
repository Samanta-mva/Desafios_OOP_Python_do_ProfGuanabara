class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def fazer_aniversario(self):
        self.idade += 1


class Aluno(Pessoa):
    def __init__(self, nome, idade, curso, turma):
        super().__init__(nome, idade)
        self.curso = curso
        self.turma = turma

    def fazer_matricula(self):
        pass


class Professor(Pessoa):
    def __init__(self, nome, idade, especializacao, nivel):
        super().__init__(nome, idade)
        self.especialidade = especializacao
        self.nivel = nivel

    def dar_aula(self):
        pass


class Funcionario(Pessoa):
    def __init__(self, nome, idade, cargo, setor):
        super().__init__(nome, idade)
        self.cargo = cargo
        self.setor = setor

    def bater_ponto(self):
        pass


a1 = Aluno('Maria', 17, 'TI', 'TI-01')
print(a1.__dict__)

p1 = Professor('Augusto', 47, 'Redes', 'Mestrado')
print(p1.__dict__)

f1 = Funcionario('Aline', 52, 'Diretora', 'Administrativo')
print((f1.__dict__))