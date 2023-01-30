#Ejercicio 10
#Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas. 
#Suele hacer venta por correo y la empresa de logística les cobra por peso de cada paquete 
#así que deben calcular el peso de los payasos y muñecas que saldrán en cada paquete a demanda. 
# cada payaso pesa 112 g y cada muñeca 75 g. Escribir un programa que lea el número de payasos
#  y muñecas vendidos en el último pedido y calcule el peso total del paquete que será enviado.

payaso_gramos = 112
muneca_gramos = 75

payasos = int(input('Cuantos payasos vendiste en el ultimo periodo? => '))
munecas = int(input('Cuantas munecas vendiste en el ultimo periodo? => '))
peso_total = (payasos * payaso_gramos) + (munecas * muneca_gramos)
print(f'El peso total del paquete a enviar es de {peso_total} gramos')

