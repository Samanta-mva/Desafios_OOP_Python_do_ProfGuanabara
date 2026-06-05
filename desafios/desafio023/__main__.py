from classes import Quadrado, Circulo

def main():
    p1 = Quadrado(20)
    print(f'Um quadrado com lados de {p1.distancia}cm tem um perímetro de {p1.perimetro()}')
    print(f'Um quadrado com lados de {p1.distancia}cm area de {p1.area()}')
    print()
    p2 = Circulo(12)
    print(f'Um círculo com raio de {p2.distancia}cm tem um perímetro de {p2.perimetro()}')
    print(f'Um círculo de raio de {p2.distancia}cm tem uma area de {p2.area()}')


if __name__ == '__main__':
    main()