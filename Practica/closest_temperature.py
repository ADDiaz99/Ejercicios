"""
Closest Temperature Codingame Puzzle
https://www.codingame.com/ide/puzzle/temperatures

Rules
Write a program that prints the temperature closest to 0 among input data. If two numbers are equally close to zero, positive integer has to be considered closest to zero (for instance, if the temperatures are -5 and 5, then display 5).
 	Game Input
    Your program must read the data from the standard input and write the result on the standard output.

    Input

    Line 1: N, the number of temperatures to analyze


    Line 2: A string with the N temperatures expressed as integers ranging from -273 to 5526

Output
Display 0 (zero) if no temperatures are provided. Otherwise, display the temperature closest to 0.
Constraints
0 ≤ N < 10000
"""

#Solution:

import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())  # the number of temperatures to analyse
temperatures = []
closest_number = 0
for i in input().split():
    
    # t: a temperature expressed as an integer ranging from -273 to 5526
    t = int(i)
    
    temperatures.append(t)

def closest_to_zero(temperatures):
    if len(temperatures) == 0:
        print(0)
    
    else:

        closest = float('inf')  # Set the initial closest value to positive infinity

        for temp in temperatures:
            if abs(temp) < abs(closest) or (abs(temp) == abs(closest) and temp > closest):
                closest = temp

        print(closest) 

closest_to_zero(temperatures)
# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

