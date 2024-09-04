"""
Programacion orientada a objetos
"""

class Carro:
    """Atributos"""
    ruedas = 4

    """Contructor: Valores que van a tener por defecto mi clase que se le instanciará a una variable"""
    def __init__(self, color, aceleracion, velocidad = 0):
        self.color = color
        self.aceleracion = aceleracion
        self.velocidad = velocidad

    """Métodos: son las funciones de la clase"""
    def acelerar(self):
        self.velocidad = self.velocidad + self.aceleracion

    def frenar(self):
        velocidad = self.velocidad - self.aceleracion
        if velocidad < 0:
            velocidad = 0

        self.velocidad = velocidad


"""Aplicando herencia"""
"""Creamos una clase hija"""

class CarroVolador(Carro):

    ruedas = 6
    def __init__(self, color, aceleracion, estadoVolando = False):
        super().__init__(color, aceleracion)
        self.estadoVolando = estadoVolando

    def vuela(self):
        self.estadoVolando = True

    def aterriza(self):
        self.estadoVolando = False


carro1 = Carro('Rojo', 45)

carroVol = CarroVolador('Blanco', 55)

carroVol.vuela()

print(carroVol.estadoVolando)

carroVol.aterriza()

print(carroVol.estadoVolando)