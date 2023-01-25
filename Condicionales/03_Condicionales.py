# Ejercicio 3 
# Escribir un programa que pida al usuario dos números y muestre por pantalla su división. 
# Si el divisor es cero el programa debe mostrar un error.

#SOLUCION:

print('=' * 30)
print( 'Vamos a hacer una division!')
print('=' * 30)
dividendo = float(input('Digita el primer numero => '))
divisor = float(input('Ahora digita el numero por que quieres dividir => '))


if divisor == 0:
    print('Syntax error papa, no se puede dividir por cero... ')
else:
    print(f'{dividendo} / {divisor} es igual a {(dividendo / divisor)}. ' )