#Escribir una función que convierta un número decimal en binario y otra 
#que convierta un número binario en decimal.

#Solucion:

def decimal_a_binario(number):
    binario = []
    
    while number >= 1:
        if number % 2 == 0:
            number = number // 2
            binario.append(0)
        else:
            number = number // 2
            binario.append(1)
    return print(binario[::-1])

decimal_a_binario(65)

def to_decimal(n):
    
    n = list(n)
    n.reverse()
    decimal = 0
    for i in range(len(n)):
        decimal += int(n[i]) * 2 ** i
    return decimal



