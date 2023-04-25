'''
Escribir un programa que cree un diccionario vacío y lo vaya llenado con 
información sobre una persona (por ejemplo nombre, edad, sexo, teléfono, correo electrónico, etc.) 
que se le pida al usuario. Cada vez que se añada un nuevo dato debe imprimirse el contenido del diccionario.
'''

#Solucion

datos = {
    'nombre' : 0,
    'edad' : 0,
    'sexo' : 0,
    'telefono' : 0,
    'correo' : 0,
}

for dato in datos:
    #print(f'El dato es {dato} y el valor es {datos[dato]}')
    datos[dato] = input(f'Cual es tu {dato}=> ')

    print(datos)
