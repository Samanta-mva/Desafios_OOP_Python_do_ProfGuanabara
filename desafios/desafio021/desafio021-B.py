from rich import print

class Caneta:
    def __init__(self, cor='azul'):
        match cor.lower().strip():
            case 'azul':
                escolha = '[blue]'
            case 'vermelho' | 'vermelha':
                escolha = '[red]'
            case 'amarelo' | 'amarela':
                escolha = '[yellow]'
            case 'verde':
                escolha = '[green]'
            case _:
                escolha = '[white]'

        self.cor = escolha
        self.tamapda = True

    def escrever(self, msg):
        if self.tamapda:
            print(f':prohibited: A {self.cor}caneta está tampada.', end='')
        else:
            print(f'{self.cor}{msg}[/]', end='')


    def tampar(self):
        self.tamapda = True


    def destampar(self):
        self.tamapda = False


    def quebrar_linha(self, qnt = 1):
        print('\n' * qnt, end='')


c1 = Caneta()
c1.escrever('Olá!')
c2 = Caneta('vermelha')
c2.escrever('Tudo bem?')
c2.quebrar_linha(2)
c3 = Caneta('amarela')
c3.destampar()
c3.escrever('Agora sim')