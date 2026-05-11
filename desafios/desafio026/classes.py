from abc import ABC, abstractmethod
from rich import print
from rich.panel import Panel


class Funcionario(ABC):
    def __init__(self, nome):
        self.nome = nome
        self.salario_bruto = 0
        self.salario_min = 1612
        self.inss = 7.5
        self.salario_liq = 0

    @abstractmethod
    def calc_salario(self):
        pass

    def analisar_salario(self):
        painel = Panel(f'{self.calc_salario()}',title='Análise de Salário', width=45)
        print(painel)


class Horista(Funcionario):
    def __init__(self, nome, valorHora, horasTrabalhadas):
        super().__init__(nome)
        valor_hora = valorHora
        horas_trabalhadas = horasTrabalhadas
        self.salario_bruto = valor_hora * horas_trabalhadas


    def calc_salario(self):
        self.salario_liq = self.salario_bruto * (1 - self.inss / 100)
        msg = f'O salário de {self.nome}(funcionário horista) é de R${self.salario_liq:.2f} e corresponde a {self.salario_liq / self.salario_min:.1f} salários mínimos.'
        return msg


class Mensalista(Funcionario):
    def __init__(self, nome, salarioBruto):
        super().__init__(nome)
        self.salario_bruto = salarioBruto
        return

    def calc_salario(self):
        self.salario_liq = self.salario_bruto * (1 - self.inss / 100)
        msg = f'O salário de {self.nome}(funcionário mensalista) é de R${self.salario_liq:.2f} e corresponde a {self.salario_liq / self.salario_min:.1f} salários mínimos.'
        return msg
