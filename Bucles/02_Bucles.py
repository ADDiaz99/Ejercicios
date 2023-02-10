#Escribir un programa que pregunte al usuario su edad y 
#muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad).

#SOLUCION:

edad = int(input('Que edad tienes? =>'))

for i in range(edad):
    print(f'Has cumplido {str(i+1)} anos!')


