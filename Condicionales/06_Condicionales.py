#Ejercicio 6 
# Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el nombre. 
# El grupo A esta formado por las mujeres con un nombre anterior a la M y los hombres con un nombre posterior a la N y el grupo B por el resto. 
# Escribir un programa que pregunte al usuario su nombre y sexo, y muestre por pantalla el grupo que le corresponde.

#SOLUCION:

name = input('Cual es tu nombre? => ')
sex = input('Eres hombre o mujer? => ')

if sex == 'hombre' :
    if name.lower() > 'n' :
        print('Eres parte del grupo A')
    
    else:
        print('Eres parte del grupo B')
else:
    if name.lower() < 'M' :
        print('Eres parte del grupo A')
    
    else :
        print('Eres parte del grupo B')
