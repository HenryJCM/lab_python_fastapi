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

print("El color de mi carro 1 es: {}".format(carro1.color))
print("La aceleracion de mi carro 1 es: {}".format(carro1.aceleracion))
print("La velocidad inicial de mi carro 1 es: {}".format(carro1.velocidad))
print("La cantidad de ruedas de mi carro 1 es: {}".format(carro1.ruedas))


carro2 = Carro('Rojo', 70)
carro2.acelerar()
print("El color de mi carro 2 es: {}".format(carro2.color))
print("La aceleracion de mi carro 2 es: {}".format(carro2.aceleracion))
print("La velocidad inicial de mi carro 2 es: {}".format(carro2.velocidad))
print("La cantidad de ruedas de mi carro 2 es: {}".format(carro2.ruedas))

"""Asignacion dinamica que solo afecta a la instancia"""
carro2.marchas = 2000
print("El nomero de marchas de mi carro 2 es: {}".format(carro2.marchas))
