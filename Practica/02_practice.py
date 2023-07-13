"""
Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user. 
Hint: how does an even / odd number react differently when divided by 2?

Extras:

If the number is a multiple of 4, print out a different message.
Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). If check divides evenly into num, tell that to the user. If not, print a different appropriate message.
"""

#Solution:

num = int(input("Let's find out if a number is even or odd, type any number => "))
check = int(input("Now a number to divide by => "))

if num % 2 == 0:
    print("This number is even")
    if num % 4 == 0:
        print("And it is a multiple of 4!")
else:    
    print("This number is odd")

if num % check == 0:
    print(f"{num} divides evenly into {check}")
else:
    print(f"{num} does not divide evenly into {check}")

