from rich import print
from rich.panel import Panel


class Gamer:
    def __init__(self, nome, nick):
        self.nome = nome
        self.nick = nick
        self.jogo_favorito = []

    def add_favorito(self, jogo):
        self.jogo_favorito.append(f':video_game: {jogo}')


    def mostra_favorito(self):
        ordenado = sorted(self.jogo_favorito)
        lista_favoritos = f'[blue]{'\n'.join(ordenado)}[/]'
        return lista_favoritos


    def ficha(self):
        painel = Panel(f'\nNome real: [black on blue] {self.nome} [/]\n\nJogos Favoritos:\n{self.mostra_favorito()}', title=f'Jogador <{self.nick}>', width=35)
        print(painel)


j1 = Gamer('Davi Amaral','blackwolf2010')
j1.add_favorito('Mario Kart')
j1.add_favorito('Sonic Evolution')
j1.ficha()
j2 = Gamer('Diogo', 'Kharuz')
j2.add_favorito('Tomb Raider')
j2.add_favorito('Call of Dut')
j2.add_favorito('LOTRO')
j2.add_favorito('Castlevania')
j2.ficha()