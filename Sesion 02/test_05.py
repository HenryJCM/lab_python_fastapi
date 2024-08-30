class Carro:
    """Esta clase esta definiendo el estado y el comportamiento de un carro"""
    ruedas = 4

    def __init__(self, color, aceleracion):
        self.color = color
        self.aceleracion = aceleracion
        self.velocidad = 0

    def acelerar(self):
        self.aceleracion = self.velocidad + self.aceleracion

    def frenar(self):
        velocidad = self.velocidad - self.aceleracion
        if velocidad < 0:
            velocidad = 0

        self.velocidad = velocidad

carro1 = Carro('azul', 40)

print("El color de mi primer carro es: {}".format(carro1.color))