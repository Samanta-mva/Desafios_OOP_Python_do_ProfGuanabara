# Declaração da Classe
class Gafanhoto:
    """
    Classe Gafanhoto
Essa classe cria um Gafanhoto que tem nome e idade;

Para criar uma nova pessoa, use:
variavel = Gafanhoto(nome, idade)
    """
    def __init__(self, nome = 'vazio', idade = 0): # Metodo Construtor / Self se refere ao objeto que chamou a classe
        # Atributos de instancia
        self.nome = nome
        self.idade= idade

    # Metodos de Instancia
    def aniversario(self):
        self.idade += 1

    def __str__(self): # Dunder Method
        return (f'{self.nome} é Gafanhoto e tem {self.idade} anos de idade.')

    def __getstate__(self):
        return f'Estado: nome = {self.nome} ; idade = {self.idade}'

# Declaração do Objeto
g1 = Gafanhoto('Maria', 17)
g1.aniversario()
print(g1)
print(g1.__dict__) # Attribut
print(g1.__getstate__()) # Method
print(g1.__class__) # Attribut 

#print(g1.__doc__) # Dunder Attribut
