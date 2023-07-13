#Create a program that asks the user to enter their name and their age. 
#Print out a message addressed to them that tells them the year that they will turn 100 years old. 
#Note: for this exercise, the expectation is that you explicitly write out the year 
#(and therefore be out of date the next year)

#Solution:

name = input("Insert your name here => ")
age = int(input("Insert your age here => "))

message = f"Hello there {name}, you will be 100 years old in {(2023 - age) + 100}! If you are lucky... \n"
print(message)

repetition = int(input("Now, tell me how many times do you want the message to appear on your screen => "))
print(message * repetition)
