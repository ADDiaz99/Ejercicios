#Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, 
# y muestre por pantalla el capital obtenido en la inversión cada año que dura la inversión.

#Solucion:
'''
money = int(input('Cuanto dinero planeas invertir? =>'))
inter = float(input('Cual es el interes anual? =>'))
num = int(input('Cuanto tiempo dura la inversion? =>'))
result = ((money * inter) / 100) * num 

print(f'La inversion total que vas a ganar es de {result}$')

'''

amount = float(input("¿Cantidad a invertir? "))
interest = float(input("¿Interés porcentual anual? "))
years = int(input("¿Años?"))
for i in range(years):
    amount *= 1 + interest / 100 
    print("Capital tras " + str(i+1) + " años: " + str(round(amount, 2)))
