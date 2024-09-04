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

carro1 = Carro('Negro', 50)

carro1.acelerar()
carro1.acelerar()
carro1.acelerar()
carro1.acelerar()

print("La velocidad actual de mi carro 1 es: {}".format(carro1.velocidad))

carro1.frenar()
carro1.frenar()

print("La velocidad actual de mi carro 1 es: {}".format(carro1.velocidad))
