#Escribir una función que reciba una muestra de números en una lista y devuelva otra lista con sus cuadrados.

#Solucion

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def elevar_al_cuadrado(numeros):
    numeros_cuadrado = []

    for numero in numeros:
        numeros_cuadrado.append(numero ** 2)

    return print(numeros_cuadrado)

elevar_al_cuadrado(numeros)
