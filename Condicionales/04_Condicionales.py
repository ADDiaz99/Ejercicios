#Ejercicio 4 
#Escribir un programa que pida al usuario un número entero y muestre por pantalla si es par o impar.

#SOLUCION:

numero = int(input('Bienvenido, digita un numero => '))

if numero % 2 == 0:
    print('Este numero es par ')
else:
    print('Este numero es impar')