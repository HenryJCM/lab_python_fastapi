"""Decoradores de Python"""

"""Creacion interna de la funcion decoradora"""

def funcionA(funcionB):

    def funcionC(*args, **kwargs):
        print("1. Antes de ejecutar la funcion a decorar")
        resultado = funcionB(*args, **kwargs)
        print("2. Esto sucede luego de ejecutar la funcion a decorar")
        return resultado

    return funcionC

@funcionA
def saludar(nombre, edad, **kwargs):
    print('Hola {}, usted tiene {} años'.format(nombre, edad))
    for key, value in kwargs.items():
        print("{} : {}".format(key, value))

nombre = input('Ingrese su nombre: ')
edad = input('Ingrese su edad: ')

saludar(nombre, edad, ciudad1="Lima", ciudad2="Tacna", ciudad3="Arequipa", ciudad4="Chiclayo")