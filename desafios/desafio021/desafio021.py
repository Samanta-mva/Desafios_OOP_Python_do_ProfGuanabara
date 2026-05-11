from rich import print

class Caneta:
    print('A caneta está tampada.')
    def __init__(self, cor):
        self.cor = cor.upper()
        self.destampada = False
        self.mensagem = ''

        if self.cor == 'VERMELHA' or self.cor == 'VERMELHO':
            self.cor = "[red]"

        if self.cor == 'AZUL':
            self.cor = "[blue]"

        if self.cor == 'VERDE':
            self.cor = "[green]"

        if self.cor == 'AMARELA' or self.cor == 'AMARELO':
            self.cor = "[yellow]"

    def destampar(self):
        self.destampada = True

    def escrever(self, texto='Vazio'):
        if self.destampada:
            self.mensagem += self.cor
            self.mensagem += texto
            print(self.mensagem, end=' ')

        else:
            print('A caneta está tampada.')

    def quebrar_linha(self, qnt):
        print('\n' * qnt)



c1 = Caneta('amarela')
c1.destampar()
c1.escrever('Olá, mundo!')
c1.quebrar_linha(3)
c2 = Caneta('azul')
c2.destampar()
c2.escrever('Tudo bem?')
c3 = Caneta('vermelha')
c3.escrever('Samanta')
c4 = Caneta('verde')
c4.quebrar_linha(1)
c4.destampar()
c4.escrever('Que cor?')
c5 = Caneta('vermelho')
c5.destampar()
c5.escrever('Testando caneta vermelha.')