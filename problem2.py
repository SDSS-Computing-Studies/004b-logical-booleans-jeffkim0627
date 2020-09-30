#! python3

"""
Problem 2
Factors are positive integers that divide evenly into another integer.
The user will enter in two numbers. Determine if the smaller is a factor of the larger
(2 marks)

inputs:
an integer
an integer

outputs:
xx is a factor of yy
xx is not a factor of yy

examples:
Enter a number: 10
Enter another number: 2
2 is a factor of 10

Enter a number: 4
Enter another number: 25
4 is not a factor of 25
"""

import math
int1 = float(input("Enter a first number"))
int2 = float(input("Enter a second number"))

if (int1 > int2) == True:
    if int1 / int2 == math.ceil(int1 / int2):
        print(str(int2) + " is a factor of " + str(int1))
    else :
        print(str(int2) + " is not a factor of " + str(int1))
elif (int2 > int1) == True:
    if int2 / int1 == math.ceil(int2 / int1):
        print(str(int1) + " is a factor of " + str(int2))
    else:
        print(str(int1) + " is not a factor of " + str(int2))
elif (int1 == int2) == True:
    print("Both numbers are factor to each other")