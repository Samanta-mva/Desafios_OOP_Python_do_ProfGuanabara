import random
from abc import ABC, abstractmethod
from random import randint
from rich import print
from rich.panel import Panel

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
        self.vida = vida
        self.golpes = []

    def atacar_alvo(self, alvo, forca):
        """
        Método utilizado para atacar um alvo.
        :param alvo: usado para definir quem será atacado
        :param forca: usado para definir qual será a força do ataque
        E por final printa as ações do ataque.
        """
        # definindo qual golpe sera aplicado de modo aleatorio
        golpe = random.choice(self.golpes)

        # dano sera aleatorio entre 0 até a forca definida do atacante
        dano = randint(0, forca)

        # chamada do metodo que recebe o dano
        alvo.receber_dano(dano)

        print( f'{self.nome}({self.vida}) atacou {alvo.nome}({alvo.vida + dano}) com um {golpe} de força {forca}\n{alvo.nome}, recebeu um dano de {dano}.\n'\
               f'{alvo.nome} ficou com {alvo.vida} de vida.')



    def receber_dano(self, dano):
        """
        Método utilizado para registrar o
        dano que o persongem levou
        :param dano: recebe o valor do dano
        causado e aplica nos pontos de vida
        do personagem alvo.
        """
        self.vida -= dano

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
        ficha = Panel(f'Player {self.nome} \nClasse {self.nome_classe} \nVida {self.vida}',
                      title='Ficha do Personagem', width= 30)

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

        # atualiza os pontos de vida somando com o valor gerado no rec_vida
        self.vida += rec_vida

        # printa a mensagem de quem e quanto foi recupera de vida
        print( f'{self.nome} usa atadura nos ferimentos e recupera {rec_vida} pontos de vida.\n'\
               f'Agora {self.nome} tem {self.vida} pontos de vida.')


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

        # atualizamos os pontos de vida anterior somados com o valor gerado em rec_vida
        self.vida += rec_vida

        # printa a mensagem de quem e quanto foi recuperado dos pontos de vida
        print( f'{self.nome} usa magia de cura e recupera {rec_vida} pontos de vida.\n'\
               f'Agora {self.nome} tem {self.vida} pontos de vida.')

