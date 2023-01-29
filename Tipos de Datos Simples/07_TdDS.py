#Ejercicio 7 
#Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros), 
#calcule el índice de masa corporal y lo almacene en una variable, 
#y muestre por pantalla la frase Tu índice de masa corporal es <imc> donde <imc> es el índice 
#de masa corporal calculado redondeado con dos decimales.

#SOLUCION

peso = float(input('Cual es tu peso? '))
estatura = float(input('Cual es tu estatura? '))
imc = (peso) / (estatura ** 2)

print('Tu indice de masa corporal es ' + str(round(imc, 2)))

