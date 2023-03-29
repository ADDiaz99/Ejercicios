#Escribir un programa que guarde en una variable el diccionario {'Euro':'€', 'Dollar':'$', 'Yen':'¥'},
#pregunte al usuario por una divisa y muestre su símbolo o un mensaje de aviso si la divisa no está en el diccionario.

#Solucion

divisas = {
    'Euro':'€',
    'Dollar':'$',
    'Yen':'¥'
}

pregunta = input("Pregunta por una divisa y te devuelvo el simbolo => ")

if pregunta.title() in divisas:
    print(divisas[pregunta.title()])

else:
    print("Esa divisa no está")