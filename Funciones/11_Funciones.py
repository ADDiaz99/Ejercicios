#Escribir un programa que reciba una cadena de caracteres y devuelva un diccionario con 
# cada palabra que contiene y su frecuencia. 


#Solucion 1:

from collections import Counter
def contador_palabras():
    frase = "En efecto, rematado ya su juicio, vino a dar en el más extraño pensamiento que jamás dio loco en el mundo, y fue que le pareció convenible y necesario, así para el aumento de su honra como para el servicio de su república, hacerse caballero andante"
    palabras = frase.split(" ")
    return print(Counter(palabras))
   
contador_palabras()


#Solucion 2: 
texto = "En efecto, rematado ya su juicio, vino a dar en el más extraño pensamiento que jamás dio loco en el mundo, y fue que le pareció convenible y necesario, así para el aumento de su honra como para el servicio de su república, hacerse caballero andante"

def counter_palabras(texto):
    texto = texto.split()
    words = {}
    for i in texto:
        if i in words:
            words[i] += 1
        else:
            words[i] = 1
    return words

print(counter_palabras(texto))