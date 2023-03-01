#Escribir un programa que pida al usuario una palabra y luego muestre por pantalla 
#una a una las letras de la palabra introducida empezando por la última.

#Solucion:

word = str(input('Introduce una palabra =>'))

for i in range(len(word) -1, -1, -1):
    print(word[i])

    
