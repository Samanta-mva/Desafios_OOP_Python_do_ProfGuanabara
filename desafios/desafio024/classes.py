from abc import ABC, abstractmethod
from time import sleep

class BebidaQuente(ABC):
    def preparar(self):
        print('-- PREPARANDO BEBIDA --')
        self.ferver()
        self.misturar()
        self.servir()
        print('-- BEBIDA PRONTA --\n')
        sleep(1)

    def ferver(self):
        sleep(1)
        print('1 - Fervendo água até 100ºC...')

    @abstractmethod
    def misturar(self):
        pass

    @abstractmethod
    def servir(self):
        pass


class Cafe(BebidaQuente):
    def misturar(self):
        super().misturar()
        sleep(2)
        print('2 - Passando a água pelo pó de café moído...')

    def servir(self):
        super().servir()
        sleep(2)
        print('3 - Servindo o café na xícara pequena...')
        sleep(1)


class Cha(BebidaQuente):
    def misturar(self):
        sleep(2)
        print('2 - Mergulhando o sachê de ervas na água...')

    def servir(self):
        sleep(2)
        print('3 - Servindo o chá na caneca de porcelana com limão...')
        sleep(1)


class Leite(BebidaQuente):
    def misturar(self):
        sleep(2)
        print('2 - Passando vapor pressurizado pelo bico do leite')

    def servir(self):
        sleep(2)
        print('3 - Servindo na caneca grande já com café...')
        sleep(1)


