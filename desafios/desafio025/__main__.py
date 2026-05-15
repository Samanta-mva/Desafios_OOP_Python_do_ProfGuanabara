from modalidade import *
from rich import print
from rich.table import Table


def main():
    distancia = int(input('Qual será a distancia do frete? \n→ km = '))
    entrega1 = Moto(distancia)
    entrega2 = Caminhao(distancia)
    entrega3 = Drone(distancia)

    tabela = Table(title='Tabela de Fretes', width=55, show_lines=True)
    tabela.add_column('Tipo do Frete')
    tabela.add_column('Distância')
    tabela.add_column('Valor')

    tabela.add_row(f'{type(entrega1).__name__}', f'{distancia}km', f'{entrega1.calc_frete()}')
    tabela.add_row(f'{type(entrega2).__name__}', f'{distancia}km', f'{entrega2.calc_frete()}')
    tabela.add_row(f'{type(entrega3).__name__}', f'{distancia}km', f'{entrega3.calc_frete()}')
    print(tabela)


if __name__ == '__main__':
    main()