from rich import print

class Funcionario:
    """
    Esta classe serve para cadastro de funcionários.
    Para registrar um novo funcionário precisa do nome, setor e cargo deste funcionário.
    """

    empresa = 'Curso em Vídeo'

    def __init__(self, nome = 'Vazio', setor = 'Setor Não Cadastrado', cargo = 'Sem Cargo'):
        self.funcionario = nome
        self.setor = setor
        self.cargo = cargo

    def apresentacao(self) -> str:
        return f':yellow_heart: Olá! Eu sou [bold blue]{self.funcionario}[/] e sou {self.cargo} do setor de {self.setor} da empresa {Funcionario.empresa}.\n'

f1 = Funcionario(nome='Samanta', cargo='Diretora', setor='Administração')
print(f1.apresentacao())

f2 = Funcionario(nome='Gustavo', cargo='Professor', setor='Programação')
print(f2.apresentacao())