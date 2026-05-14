from abc import ABC, abstractmethod
from random import randint, choice
from rich import print
from rich.panel import Panel
import sys



class Personagem(ABC):
    """
    Esta é uma classe abstrata que serve como base
    para criar outras classes de personagens.
    Tem os métodos atacar_alvo, receber_dano e o
    método abstrato curar.
    """

    # primeiro chama-se os atributos de inicialização
    def __init__(self, nome, vida):
        self.nome = nome
        self.vidaMax = vida
        self.vidaAtual = self.vidaMax
        self.golpes = []
        self.alvo = ''

    def atacar_alvo(self, alvo, forca):
        """
        Método utilizado para atacar um alvo.
        :param alvo: usado para definir quem será atacado
        :param forca: usado para definir qual será a força do ataque
        E por final printa as ações do ataque.
        """

        # define o alvo
        alvo = alvo

        # definindo qual golpe sera aplicado de modo aleatorio
        golpe = choice(self.golpes)

        # dano sera aleatorio entre 0 até a forca definida do atacante
        dano = randint(0, forca)

        print(f'[bold bright_white]{self.nome}({self.vidaAtual}) atacou {alvo.nome}({alvo.vidaAtual}) com um [bold]{golpe}[/] de força {forca}\n[/][red]{alvo.nome}, recebeu um dano de {dano}.[/]')

        # chamada do metodo que recebe o dano
        alvo.receber_dano(dano, alvo)

        print(f'[yellow]{alvo.nome} ficou com {alvo.vidaAtual} de vida.\n[/]')


    def receber_dano(self, dano, alvo):
        """
        Método utilizado para registrar o
        dano que o persongem levou
        :param dano: recebe o valor do dano
        causado e aplica nos pontos de vida
        do personagem alvo.
        """
        # verifica se ainda restam pontos de vida
        if dano < alvo.vidaAtual:
            self.vidaAtual -= dano
            return self.vidaAtual
        else:
            print(f'[white]-- O personagem não resistiu aos ferimentos e perdeu a batalha --[/]\n')
            fim_de_jogo()


    @abstractmethod
    def curar(self):
        """
        Este é um método abstrato que registra
        de forma particular e individual em
        cada classe derivada de personagem um
        valor de cura dos pontos de vida de um
        personagem que varia de acordo com o
        que será determinado em sua classe.
        """
        pass

    def mostrar_ficha(self):
        ficha = Panel(f'[bright_white]Player {self.nome}\n'
                      f'Classe {self.nome_classe}\n'
                      f'Vida {self.vidaAtual}[/]',
                      title='[bright_white]Ficha do Personagem[/]', width= 30)

        print(ficha)


class Guerreiro(Personagem):
    """
    Esta é uma classe derivada de Personagem.
    """
    # primeiro definimos os atributos de inicialização
    def __init__(self, nome, vida):
        # super para puxar os atributos da classe superior(Personagem)
        super().__init__(nome, vida)

        # definimos o nome da classe
        self.nome_classe = 'Guerreiro'

        # definimos os golpes que esta classe possui
        self.golpes = ['SOCO', 'CHUTE', 'CABEÇADA', 'GANCHO']

    # método curar que recupera os pontos de vida
    def curar(self):
        # a recuperação será aleatória entre dois valores definidos aqui
        rec_vida = randint(50, 200)

        # verifica se os pontos a serem recuperados não é maior que o
        # maximo de vida e então aplica a recuperação
        if self.vidaAtual <= 0:
            pass
        elif rec_vida + self.vidaAtual >= self.vidaMax:
            self.vidaAtual = self.vidaMax
            return self.vidaAtual
        elif rec_vida + self.vidaAtual <= self.vidaMax:
            self.vidaAtual += rec_vida
            return self.vidaAtual

        # printa a mensagem de quem e quanto foi recupera de vida
        print( f'[bold green]{self.nome} usa atadura nos ferimentos e recupera {rec_vida} pontos de vida.\n[/]'\
               f'[yellow]Agora {self.nome} tem {self.vidaAtual} pontos de vida.\n[/]')


class Mago(Personagem):
    """
    Esta é uma classe derivada de Personagem.
    """
    # primeiro definimos os atributos de inicialização
    def __init__(self, nome, vida):
        # super para puxar da classe mãe os atributos padrão da classe superior(Personagem
        super().__init__(nome, vida)

        # definimos o nome da classe
        self.nome_classe = 'Mago'

        # definimos os golpes que o personagem tem
        self.golpes = ['CAJADADA', 'PONTAPÉ', 'BOLA DE FOGO']

    # método curar que recupera od pontos de vida do personagem
    def curar(self):
        # definimos que a recuperação será aleatória entre dois valores
        rec_vida = randint(10,500)

        # variavel que soma os pontos a ser recuperado com a vida atual
        recuperado = self.vidaAtual + rec_vida

        # verifica se os pontos a serem recuperados não é maior que o
        # maximo de vida e então aplica a recuperação
        if recuperado >= self.vidaMax:
            rec_vida = self.vidaMax - self.vidaAtual
            self.vidaAtual = self.vidaMax

        elif recuperado <= self.vidaMax:
            self.vidaAtual += rec_vida


        # printa a mensagem de quem e quanto foi recuperado dos pontos de vida
        print( f'[bold green]{self.nome} usa magia de cura e recupera {rec_vida} pontos de vida.\n[/]'\
               f'[yellow]Agora {self.nome} tem {self.vidaAtual} pontos de vida.\n[/]')
        return self.vidaAtual


def fim_de_jogo():
    print('FIM DE JOGO')
    sys.exit()