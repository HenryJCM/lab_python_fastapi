"""Decoradores de Python"""

"""Creacion interna de la funcion decoradora"""

def funcionA(funcionB):

    def funcionC():
        print("1. Antes de ejecutar la funcion a decorar")
        funcionB()
        print("2. Esto sucede luego de ejecutar la funcion a decorar")

    return funcionC()    

@funcionA
def saludo():
    print("Hola Pythonistas")

#saludo()