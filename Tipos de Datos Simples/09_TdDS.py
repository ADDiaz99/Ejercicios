#Ejercicio 9
#Escribir un programa que pregunte al usuario una cantidad a invertir, 
#el interés anual y el número de años, y muestre por pantalla el capital obtenido en la inversión.

inversion = int(input('Ingresa una cantidad para invertir => '))
int_anual = float(input('Cual es el interes anual? '))
tiempo = int(input('Cuantos años? '))

capital = str(round(inversion * (int_anual / 100 + 1) ** tiempo, 2))

print(f'El capital obtenido de tu inversion sera de {capital}')

