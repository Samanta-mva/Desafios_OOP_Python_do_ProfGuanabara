from classes import *

def main():
    f1 = Horista( 'Paulo', 25, 250)
    # print(f1.calc_salario())
    f1.analisar_salario()


    f2 = Mensalista('Amanda', 9500)
    # print(f2.calc_salario())
    f2.analisar_salario()

if __name__ == '__main__':
    main()