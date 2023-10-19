#Fizzbuzz.py
#Numbers divisible by 3 = fizz, by 5 = buzz, by 3 and 5 = fizzbuzz.

def fizzbuzz():

    for i in range(101):
        if i % 3 == 0 and i % 5 == 0:
            print("fizzbuzz")
            continue

        elif i % 5 == 0:
            print("buzz")
            continue
        
        elif i % 3 == 0:
            print("fizz")
            continue

        print(i)

#Starting the program
fizzbuzz()
