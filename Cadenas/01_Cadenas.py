#Escribir un programa que pregunte el nombre del usuario en la consola y un número entero e 
#imprima por pantalla en líneas distintas el nombre del usuario tantas 
#veces como el número introducido.

#SOLUCION:

name = input('Cual es tu nombre? =>')
num = int(input('Cuantas veces quieres mostrarlo? =>'))

print((name + '\n') * (num))


