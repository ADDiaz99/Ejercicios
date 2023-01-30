#Ejercicio 12
# Una panadería vende barras de pan a 3.49€ cada una. 
# El pan que no es el día tiene un descuento del 60%. 
# Escribir un programa que comience leyendo el número de barras vendidas que no son del día. 
# Después el programa debe mostrar el precio habitual de una barra de pan, 
# el descuento que se le hace por no ser fresca y el coste final total.
ventas = int(input('Cuantas barras de pan viejo vendiste? '))
pan = 3.49
descuento = 0.6
pan_viejo = descuento * 3.49 / 100 
precio = ventas * pan * (1 - descuento)
print('El coste de una barra fresca es de ' + str(pan) + '$')
print('El descuento por una barra vieja es de ' + str(descuento * 100) + '%')
print('El precio final es de ' + str(round(precio, 2)) + '$')
