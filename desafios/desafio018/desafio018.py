from rich import print
from rich.panel import Panel

class Churrasco:
    def __init__(self, titulo='Sem Título', qntPessoas=0 ):
        self.titulo = titulo
        self.qnt = qntPessoas
        self.consumoKg = 400 * qntPessoas
        self.custoTotal = self.consumoKg / 1000 * 82.40
        self.custoPessoa = self.custoTotal / self.qnt

    def analisar(self):
        self.mensagem = (f'Analisando [green]{self.titulo}[/] com [blue]{self.qnt} convidados[/]\n'
                    f'Cada participante comerá 0.4Kg de carne e cada Kg custa R$82.40\n'
                    f'Recomendo [blue]comprar {self.consumoKg}Kg[/] de carne\n'
                    f'O custo total será de [green]R${self.custoTotal:,.2f}[/]\n'
                    f'Cada pessoa pagará [yellow]R${self.custoPessoa:,.2f}[/] para participar')
        painel = Panel(self.mensagem, title=self.titulo)
        return painel


c1 = Churrasco('Churras dos Amigos', 15)
print(c1.analisar())

c2 = Churrasco('Festa de fim de Ano', 80)
print(c2.analisar())