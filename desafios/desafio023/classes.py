from abc import ABC, abstractmethod
from math import pi

class Poligono(ABC):
    def __init__(self, distancia):
        self.distancia = distancia

    @abstractmethod
    def perimetro(self):
        pass

    @abstractmethod
    def area(self):
        pass


class Quadrado(Poligono):
    def perimetro(self):
        super().__init__(self.distancia)
        return f'{float(4 * self.distancia):.1f}cm.'

    def area(self):
        super().__init__(self.distancia)
        return f'{float(self.distancia ** 2):.1f}cm²'


class Circulo(Poligono):
    def perimetro(self):
        super().__init__(self.distancia)
        return f'{2 * pi * float(self.distancia):.1f}cm.'

    def area(self):
        super().__init__(self.distancia)
        return f'{pi * self.distancia ** 2:.1f}cm².'


