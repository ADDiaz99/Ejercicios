#Escribir una función que reciba un número entero positivo y devuelva su factorial.

#Solucion:

#5! = 1x2x3x4x5 = 120
#syntax of range is (start, stop, step) 
def factorial(x):
    resultado = 1
    for i in range(2, x + 1):
        resultado *= i
    return resultado

print(factorial(5))

