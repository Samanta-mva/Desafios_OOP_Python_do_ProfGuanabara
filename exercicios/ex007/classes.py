# Importando a biblioteca para criar classes abstratas
from abc import ABC, abstractmethod

#a classe Pessoa herdando uma classe abstrata (ABC)
class Pessoa(ABC):
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def fazer_aniversario(self):
        self.idade += 1

    # Definindo um metodo abstrato
    @abstractmethod
    def estudar(self):
        pass


class Aluno(Pessoa):
    def __init__(self, nome, idade, curso, turma):
        super().__init__(nome, idade)
        self.curso = curso
        self.turma = turma

    def fazer_matricula(self):
        pass

    def estudar(self):
        print(f'O aluno {self.nome} está estudando {self.curso}.')


class Professor(Pessoa):
    def __init__(self, nome, idade, especializacao, nivel):
        super().__init__(nome, idade)
        self.especialidade = especializacao
        self.nivel = nivel

    def dar_aula(self):
        pass

    def estudar(self):
        print(f'O professor {self.nome} está estudando {self.especialidade}.')


class Funcionario(Pessoa):
    def __init__(self, nome, idade, cargo, setor):
        super().__init__(nome, idade)
        self.cargo = cargo
        self.setor = setor

    def bater_ponto(self):
        pass

    def estudar(self):
        print(f'O funcionário {self.nome} está estudando {self.cargo}.')
