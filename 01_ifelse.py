"""
IF (Condicion):
    (Esto pasa)

(Si lo de arriba no pasa entonces ->)ELSE:

"""
from math import *
#String = Cadena de caracteres = ""
#INT = numero entero
#FLOAT = numero decimal
"""
numero = int(input("Inserta un numero -> "))

if numero % 2 == 0:
    print("Es un numero par")
elif numero % 2 != 0:
    print("Es un numero impar")



if numero % 2 == 0:
    print("Es un numero par")
else:
    print("Es un numero impar")
"""

#EJERCICIO: 
#Vas a crear dos variables, que le permitan al usuario poner la edad de las dos personas
#Despues, vas a crear un algoritmo, que me diga quien es mayor de los dos.

usuario1 = int (input("Digite su edad ->"))
usuario2 = int (input("Digite su edad ->"))
"""
if usuario1 > usuario2:
    print(" Usuario1 es mayor que usuario 2")
elif usuario1 < usuario2:
    print(" Usuario02 es mayor que usuario01")
"""

if usuario1 > usuario2:
    print(" Usuario1 es mayor que usuario2")
elif usuario1 == usuario2:
    print(" Usuario01 es igual que usuario2")

else:
    print(" Usuario02 es mayor que usuario01")