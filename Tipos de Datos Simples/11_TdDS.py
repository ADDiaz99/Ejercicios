#Ejercicio 11 
# Imagina que acabas de abrir una nueva cuenta de ahorros que te ofrece el 4% de interés al año. 
# Estos ahorros debido a intereses, que no se cobran hasta finales de año, se te añaden al balance 
# final de tu cuenta de ahorros. Escribir un programa que comience leyendo la cantidad de dinero 
# depositada en la cuenta de ahorros, introducida por el usuario. Después el programa debe calcular 
# y mostrar por pantalla la cantidad de ahorros tras el primer, segundo y tercer años. Redondear 
# cada cantidad a dos decimales.

dinero = int(input('Ingresa una cantidad para invertir => '))
int_anual = 4

capital_1 = str(round(dinero * (int_anual / 100 + 1) ** 1, 2))
capital_2 = str(round(dinero * (int_anual / 100 + 1) ** 2, 2))
capital_3 = str(round(dinero * (int_anual / 100 + 1) ** 3, 2))

print(f'La cantidad de ahorros es la siguiente:\nFirst year => {capital_1}$\nSecond year => {capital_2}$\nThird year => {capital_3}$')
