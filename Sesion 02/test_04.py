"""Funciones"""

var_1 = 60
var_2 = 40

def sumar(a, b):
    return a + b

resultado = sumar(var_1, var_2)

print("El resultado es: {}".format(resultado))

def sumarDefault(number1, number2 = 20):
    return number1 + number2

print(sumarDefault(10, 15))
print(sumarDefault(10))