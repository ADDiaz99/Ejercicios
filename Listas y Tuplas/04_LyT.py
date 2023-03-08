#Escribir un programa que pregunte al usuario los números ganadores de la lotería primitiva, 
#los almacene en una lista y los muestre por pantalla ordenados de menor a mayor.

#Solucion:



numeros = []
for i in range(6):
    numeros.append(int(input('Cuales son los numeros ganadores de la loteria? ')))
numeros.sort()
print(f'Los numeros ganadores de la loteria en orden son => {numeros}')

