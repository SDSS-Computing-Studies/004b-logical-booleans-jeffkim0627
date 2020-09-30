"""
Problem 1
Ask the user to enter a number.
The number is considered "frue" if it is
divisible by 6, but not divisible by 8.
State whether the number is "frue" 
(2 marks)

Inputs:
a number

Outputs:
xx is frue
xx is not frue

example:
Enter a number: 48
48 is frue.
"""

#! python3

import math
number = float(input("Enter a number"))
if (number / 6 == math.ceil(number / 6)) and (number / 8 != math.ceil(number/8)):
    print(str(number) + " is frue")
else:
    print(str(number) + " is not frue")