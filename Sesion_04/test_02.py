"""Decoradores de Python"""

"""Creacion interna de la funcion decoradora"""

def funcionA(funcionB):

    def funcionC(*args):
        print("1. Antes de ejecutar la funcion a decorar")
        resultado = funcionB(*args)
        print("2. Esto sucede luego de ejecutar la funcion a decorar")
        return resultado

    return funcionC

@funcionA
def suma(a, b):
    print(a + b)

suma(30,100)