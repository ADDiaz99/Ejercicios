#Escribir un programa que pida al usuario una palabra y la muestre por pantalla 10 veces.

#SOLUCION:

word = input('Di una palabra =>')
print((word + '\n') * 10)

#SOLUCION 2:

word = input("Introduce una palabra: ")
for i in range(10):
    print(word)



