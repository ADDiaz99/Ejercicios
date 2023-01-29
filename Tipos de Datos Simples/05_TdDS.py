#Ejercicio 5 
#Escribir un programa que pregunte al usuario por el número de horas trabajadas y el coste por hora. 
#Después debe mostrar por pantalla la paga que le corresponde.

#SOLUCION:

horas = int(input('Cuantas horas trabajaste? '))
salario = int(input('Cuanto cobras por hora? '))
pago = horas * salario

print(f'La paga que te corresponde es de {pago}$')


