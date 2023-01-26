#Ejercicio 7 
# Los tramos impositivos para la declaración de la renta en un determinado país son los siguientes:

#Renta	Tipo impositivo
#Menos de 10000€	5%
#Entre 10000€ y 20000€	15%
#Entre 20000€ y 35000€	20%
#Entre 35000€ y 60000€	30%
#Más de 60000€	45%
#Escribir un programa que pregunte al usuario su renta anual y muestre por pantalla el tipo impositivo que le corresponde.

#SOLUCION 1:

renta = int(input('Cual es tu renta anual? => '))

if renta <= 9999 :
    print('Tu tipo impositivo es del 5% ')

elif renta >= 10000 and (renta <= 19999) :
    print('Tu tipo impositivo es del 15% ')

elif renta >= 20000 and (renta <= 34999) : 
    print('Tu tipo impositivo es del 20% ')

elif renta >= 35000 and (renta <= 59999) :
    print('Tu tipo impositivo es de 30%')

else:
    print('Tu renta es mayor a 60000$ y por ende tu tipo impositivo es del 45% ')


#SOLUCION 2:

renta = float(input("¿Cuál es tu renta anual? "))

if renta < 10000:
    tipo = 5
elif renta < 20000:
    tipo = 15
elif renta < 35000:
    tipo = 20
elif renta < 60000:
    tipo = 30
else:
    tipo = 45

print("Tienes que pagar ", renta * tipo / 100, "€", sep='')