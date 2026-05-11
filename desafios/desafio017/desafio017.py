from rich import print
from rich.panel import Panel

class Produto:
    def __init__(self, nome='Sem Nome', preco=''):
        self.produto = nome
        self.valor = 'R$ '+ str(preco)

    def etiqueta(self):
        self.etiqueta = Panel(f'{self.produto:^32}\n{'-'*31}\n{self.valor:.^31}',title='Produto', width=35)
        return self.etiqueta


p1 = Produto('Mouse',10.23)
print(p1.etiqueta())

p2 = Produto('iPhone 17 Pro Max', 25000.85)
print(p2.etiqueta())