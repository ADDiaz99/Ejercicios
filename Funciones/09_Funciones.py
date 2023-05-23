#Escribir una función que calcule el máximo común divisor de dos números y 
#otra que calcule el mínimo común múltiplo.

#Solucion:

def maximo_comun_divisor(num1, num2):
    """Función que calcula el máximo común divisor de dos números.
    Parámetros:
        - n: Es un número entero.
        - m: Es un número entero.
    Devuelve:
        El máximo común divisor de n y m.
    """
    rest = 0
    while(num2 > 0):
        rest = num2
        num2 = num1 % num2
        num1 = rest
    return num1

def mcm(n, m):
    """Función que calcula el mínimo común múltiplo de dos números.
    Parámetros:
        - n: Es un número entero.
        - m: Es un número entero.
    Devuelve:
        El mínimo común múltiplo de n y m.
    """
    if n > m:
        greater = n
    else:
        greater = m
    while (greater % n != 0) or (greater % m != 0):
        greater += 1
    return greater

print(maximo_comun_divisor(18, 24))
