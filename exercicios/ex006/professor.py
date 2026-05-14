from pessoa import Pessoa

class Professor(Pessoa):
    def __init__(self, nome, idade, especializacao, nivel):
        super().__init__(nome, idade)
        self.especialidade = especializacao
        self.nivel = nivel

    def dar_aula(self):
        pass

