# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
"""
Example of output:
(2,2)=
OO
OO
-----------------
(4,1)=
O
O
O
O
"""
height = int(input("How tall do you want your pattern? -->"))
width = int(input("How wide do you want your pattern? -->"))

def printzero(height, width):
    
    for i in range(height):
        print("O" * width)

printzero(height, width)
