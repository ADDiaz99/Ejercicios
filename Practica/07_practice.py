"""
Ask the user for a string and print out whether this string is a palindrome or not.
 (A palindrome is a string that reads the same forwards and backwards.)
"""

#Solution

string = str(input("Enter a word to check if it's a palindrome or not => "))

if string == string[::-1]:
    print("This word is a palindrome!")
else:
    print("This word is NOT a palindrome")