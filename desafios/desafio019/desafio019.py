from rich import print

class Livro:
    def __init__(self, titulo='Sem Titulo', paginas=2):
        self.titulo = titulo
        self.maxPaginas = paginas
        self.pagina_atual = 1

        print(f':open_book: [blue]Você acabou de abrir o livro [red]"{self.titulo.title()}"[/red] que tem [green]{self.maxPaginas} páginas[/green] no total.\n\nAgora você está na [yellow]página 1.[/yellow][/]')


    def avancar_paginas(self, avancou=1):
        ate_pagina = self.pagina_atual + avancou + 1

        if self.maxPaginas < ate_pagina:
            ate_pagina = self.maxPaginas + 1
            avancou = ate_pagina - self.pagina_atual - 1


        for pagina in range(self.pagina_atual, ate_pagina ):
            print(f'Pág{pagina}', end=' → ')
            self.pagina_atual = pagina

        print(f'[blue]Você avançou {avancou} páginas e agora está na [yellow]página {self.pagina_atual}[/yellow][/blue]')

        if self.maxPaginas + 1 == ate_pagina:
            print(f':closed_book: [red]Parabéns, você terminou o livro {self.titulo.title()}.[/]')


l1 = Livro('10 coisas que aprendi',50)
l1.avancar_paginas(10)
l1.avancar_paginas(18)
l1.avancar_paginas(25)
l1.avancar_paginas(15)