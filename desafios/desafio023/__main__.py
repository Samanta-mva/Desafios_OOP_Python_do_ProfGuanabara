from classes import Quadrado, Circulo

def main():
    p1 = Quadrado(20)
    print(f'O perímetro é de {p1.perimetro()}')
    print(f'A area é de {p1.area()}')
    print()
    p2 = Circulo(10)
    print(f'O perímetro é de {p2.perimetro()}')
    print(f'A area é de {p2.area()}')


if __name__ == '__main__':
    main()