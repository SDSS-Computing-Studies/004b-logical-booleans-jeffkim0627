#! python3
"""
Ask the user to enter a number. 
Tell them if the number is a positive integer
(2 points) 

inputs:
a number of any type

outputs:
xx is a positive integer.
xx is not a positive integer

example:
Enter a number: -3
-3 is not a positive integer
"""
import math
number = float(input("Enter a number"))
value = math.ceil(number)
if number == abs(value):
    print("The number is a positive integer")
else:
    print("The number is not an positive integer")