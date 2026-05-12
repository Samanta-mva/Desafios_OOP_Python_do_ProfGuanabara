from personagens import *


def main():
    player1 = Guerreiro('Kratos', 2000)
    print()
    player2 = Mago('Merlin', 3000)

    player2.mostrar_ficha()
    player1.mostrar_ficha()

    print()
    player1.atacar_alvo(player2, 1000)
    print()
    player2.curar()

    print()
    player2.mostrar_ficha()
    player1.mostrar_ficha()

if __name__ == '__main__':
    main()