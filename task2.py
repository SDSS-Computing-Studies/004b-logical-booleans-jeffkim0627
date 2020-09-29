#! python3
# Task2.py

"""
Ask the user to enter a number.
Tell them if the number is both a perfect square and a perfect cube.
(2 points) 

Inputs:
number

Outputs:
xx is both a perfect square and a perfect cube.
xx is only a perfect square.
xx is only a perfect cube.

Example:
Enter a number: 8
8 is only a perfect cube.
"""
import math
number = float(input("Enter a number"))
if number**(1/2) == math.ceil(number**(1/2)):
    print(str(number) + " is a perfect square")
elif number**(1/3) == math.ceil(number**(1/3)):
    print(str(number) + " is a perfect cube")
elif (number**(1/2) == math.ceil(number**(1/2))) and (number**(1/3) == math.ceil(number**(1/3))):
    print(str(number) + " is both a perfect square and a perfect cube")
else :
    print(str(number) + " is not a perfect square and a perfect cube")