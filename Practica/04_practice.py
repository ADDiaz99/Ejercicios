"""
Create a program that asks the user for a number and then prints out a list of all the divisors of that number. 
(If you dont know what a divisor is, it is a number that divides evenly into another number. 
For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)
"""

#Solution: 

num = int(input("Give me a number and i'll print all the divisors that it has => "))
divisors = []
number_list = range(1, num + 1)

for i in number_list:
    if num % i == 0:
        divisors.append(i)
print(f"The divisors of {num} are:\n {divisors}")

