# Declaração da Classe
class Gafanhoto:
    def __init__(self): # Metodo Construtor / Self se refere ao objeto que chamou a classe
        # Atributos de instancia
        self.nome = ''
        self.idade= 0

    # Metodos de Instancia
    def aniversario(self):
        self.idade += 1

    def mensagem(self):
        return f'{self.nome} é Gafanhoto e tem {self.idade} anos de idade.'


# Declaração do Objeto
g1 = Gafanhoto()
g1.nome = 'Maria'
g1.idade = 17
g1.aniversario()
print(g1.mensagem())

g2 = Gafanhoto()
g2.nome = 'Mauro'
g2.idade = 53
g2.aniversario()
print(g2.mensagem())