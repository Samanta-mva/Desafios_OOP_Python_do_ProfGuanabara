from personagens import *


def main():
    player1 = Guerreiro('Kratos', 2000)
    player2 = Mago('Merlin', 3000)

    player1.mostrar_ficha()
    player2.mostrar_ficha()

    player1.atacar_alvo(player2, 4000)
    player2.atacar_alvo(player1, 3000)
    player2.curar()

if __name__ == '__main__':
    main()