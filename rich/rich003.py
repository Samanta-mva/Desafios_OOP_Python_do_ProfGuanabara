from rich import print
from rich.table import Table

tabela = Table(title='Tabela de Preços')

tabela.add_column('Produto', justify='right', style='red')
tabela.add_column('Valor', justify='center', style='blue')

tabela.add_row('Lápis', 'R$ 1,50')
tabela.add_row('Borracha', '[green]R$ 2,99[/]')

print(tabela)