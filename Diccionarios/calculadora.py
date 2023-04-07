#Calculadora de dos digitos 

def suma(a, b):
    c = a + b
    return c

def resta(a, b):
    c = a - b
    return c

def multiplicacion(a, b):
    c = a * b
    return c

def division(a, b):
    c = a / b
    return c

print("*****Bienvenido a la calculadora de dos digitos*****")
print("*" * 52)
print('\nSelecciona el tipo de operacion que deseas realizar: ')
print('1. Suma\n2. Resta\n3. Multiplicacion\n4. Divison')
decision = int(input("=> "))
    

while decision >= 1 and decision <= 4:
    a = int(input("Inserta el primer digito => "))
    b = int(input("Inserta el segundo digito => "))

    if decision == 1:
        print(suma(a, b))
        break
    elif decision == 2:
        print(resta(a, b))
        break
    elif decision == 3:
        print(multiplicacion(a, b))
        break
    elif decision == 4:
        print(division(a, b))
        break
if decision >= 5:
    print("Ese numero no esta en el menu, vuelve a intentarlo")












