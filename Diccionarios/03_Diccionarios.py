#Escribir un programa que guarde en un diccionario los precios de las frutas de la tabla, 
#pregunte al usuario por una fruta, un número de kilos y muestre por pantalla el precio de ese número de kilos de fruta.
#Si la fruta no está en el diccionario debe mostrar un mensaje informando de ello.

#Fruta	Precio
#Plátano	1.35
#Manzana	0.80
#Pera	0.85
#Naranja	0.70

#Solucion 1:

frutas = {
    'platano' : 1.35,
    'manzana' : 0.80,
    'pera' : 0.85,
    'naranja' : 0.70
}

fruta = input("Que fruta te gustaria comprar? => ")
solicitud = float(input("Cuantos kilos vas a comprar? => "))

if fruta in frutas:
    print(f'El precio total es de {frutas[fruta] * solicitud}$ ')
else:
    print("Esa fruta no esta disponible ")


#Solucion 2:

frutas = {'Plátano':1.35, 'Manzana':0.8, 'Pera':0.85, 'Naranja':0.7}
fruta = input('¿Qué fruta quieres? ').title()
kg = float(input('¿Cuántos kilos? '))
if fruta in frutas:
    print(kg, 'kilos de', fruta, 'valen', frutas[fruta]*kg, '€')
else: 
    print("Lo siento, la fruta", fruta, "no está disponible.")