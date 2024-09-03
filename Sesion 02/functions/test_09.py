"""Programacion funcional con Python"""

var_1 = 50
var_2 = 120

def sumar(a, b):
    return a + b


# def sumar(a, b):
#    suma = a + b
#    return suma

resultado = sumar(var_1, var_2)
"""Output: Lo que retorna la funcion"""
print("El resultado es: {}".format(resultado))

resultado2 = sumar(90.7, 150.89)
print("El resultado es: {}".format(resultado2))