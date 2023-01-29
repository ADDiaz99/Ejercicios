#Ejercicio 6
#Escribir un programa que lea un entero positivo, N, introducido por el usuario y después muestre en pantalla la suma 
#de todos los enteros desde 1 hasta N. La suma de los N primeros enteros positivos puede ser calculada de la siguiente forma:

#SOLUCION

n = int(input('Introduce un numero entero'))

suma = (n * (n + 1)) / 2

print('La suma de los primeros numeros enteros desde 1 hasta ' + str(n) + ' es ' + str(suma))




