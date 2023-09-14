"""
Time for some fake graphics! Let’s say we want to draw game boards that look like this:

 --- --- --- 
|   |   |   | 
 --- --- ---  
|   |   |   | 
 --- --- ---  
|   |   |   | 
 --- --- --- 

 This one is 3x3 (like in tic tac toe). Obviously, they come in many other sizes (8x8 for chess, 19x19 for Go, and many more).

Ask the user what size game board they want to draw, and draw it for them to the screen using Python's print statement.

"""
#Solution:
#height = int(input("Height of the board? -->"))
#width = int(input("Width of the board? -->"))

board = " ---\n|   |\n ---"



def BoardSquare(height, width):
    for i in range(height):
        print((board) * width)


BoardSquare(3,3)