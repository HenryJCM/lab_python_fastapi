"""
Programacion funcional en Python

Ejercicio en clase
"""

"""
Requisitos
- Solicitar al usuario 4 numeros por consola
- Crear una funcion que devuelva cual es el mayor numero de los 4 ingresado por el usuario
- Finalmente elevar al cubo este resultado
"""

def mayor(numeros):
    return max(numeros)

numeros = []
contador = 1
while True:
        numeros.append(float(input("Ingrese un numero: ")))
        if contador == 4:
            break
        contador += 1

mayor = mayor(numeros)
print("El numero mayor es {}".format(mayor))
print("El cubo de {numero} es {al_cubo}".format(numero=mayor,al_cubo=mayor ** 3))