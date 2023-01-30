#Ejercicio 8 Escribir un programa que pida al usuario dos números enteros y muestre por pantalla la
#  <n> entre <m> da un cociente <c> y un resto <r> donde <n> y <m> son los números introducidos 
# por el usuario, y <c> y <r> son el cociente y el resto de la división entera respectivamente.


n = int(input('Introduce el dividendo => '))
m = int(input('Introduce el divisor => '))

cociente = n / m
residuo = n % m

print(f'El cociente de la operacion es {cociente} y el residuo es de {residuo} ')

