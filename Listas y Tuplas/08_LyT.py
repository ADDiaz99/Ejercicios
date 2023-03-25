#Escribir un programa que pida al usuario una palabra y muestre por pantalla si es un palíndromo

#Solucion

palabra = input(str("Introduce una palabra para verificar si es palindromo =>"))

def reverse(palabra):
    palabra = palabra[::-1]
    return palabra

if reverse(palabra) == palabra:
    print("Esta palabra es un palindromo")
else:
    print("No es un palindromo")


#Solucion 2

word = input("Introduce una palabra: ")
reversed_word = word
word = list(word)
reversed_word = list(reversed_word)
reversed_word.reverse()
if word == reversed_word:
    print("Es un palíndromo")
else:
    print("No es un palíndromo")