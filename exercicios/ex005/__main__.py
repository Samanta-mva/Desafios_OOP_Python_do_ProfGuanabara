from classes_ex005 import Aluno, Professor, Funcionario

# Modularizando corretamente com __main__()
def __main__():
    a1 = Aluno('Maria', 17, 'TI', 'TI-01')
    print(a1.__dict__)

    p1 = Professor('Augusto', 47, 'Redes', 'Mestrado')
    print(p1.__dict__)

    f1 = Funcionario('Aline', 52, 'Diretora', 'Administrativo')
    print(f1.__dict__)

# Por segurança verifica se o nome do arquivo é __main__
if __name__ == '__main__':
    #se for executa o metodo __main__
    __main__()