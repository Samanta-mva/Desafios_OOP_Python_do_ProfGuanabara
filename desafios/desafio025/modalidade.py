from abc import ABC, abstractmethod

class Transporte(ABC):
    def __init__(self, distancia):
        self.distancia = distancia
        self.frete = 0

    @abstractmethod
    def calc_frete(self):
        pass


class Moto(Transporte):
    def calc_frete(self):
        super().__init__(self.distancia)
        fator = 0.5
        self.frete = f'R${self.distancia * fator:.2f}'
        return self.frete


class Caminhao(Transporte):
    def calc_frete(self):
        super().__init__(self.distancia)
        fator = 1.2
        if self.distancia >= 50:
            self.frete = f'RS{self.distancia * fator:.2f}'
            return self.frete

        else:
            return 'Distância mínima 50km.'


class Drone(Transporte):
    def calc_frete(self):
        super().__init__(self.distancia)
        fator = 9.5
        if self.distancia <= 10:
            self.frete = f'R${self.distancia * fator:.2f}'
            return self.frete

        else:
            return 'Distância máxima 10km.'
