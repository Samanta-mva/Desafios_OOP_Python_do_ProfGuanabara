from classes import *


def main():
    dist = 10
    entrega = Moto(dist)
    print(f'Frete de {type(entrega).__name__} em {dist}km = {entrega.calc_frete()}')

    entrega2 = Caminhao(dist)
    print(f'Frete de {type(entrega2).__name__} em {dist}km = {entrega2.calc_frete()}')

    entrega3 = Drone(dist)
    print(f'Frete de {type(entrega3).__name__} em {dist}km = {entrega3.calc_frete()}')


if __name__ == '__main__':
    main()