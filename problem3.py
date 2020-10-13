#! python3
"""
Problem 3
Pythagorean triples are sets of 3 integers such that the squares of the 2 smaller numbers is equal to the square of the third.
Ask the user to enter in 3 numbers, in any order.  Order the numbers from smallest to largest.
Determine if they form a Pythagorean triple. 
(2 marks)

Inputs:
an integer
an integer
an integer

Outpus:
xx,yy,zz form a Pythagorean Triple
xx,yy,zz do not form a Pythagorean Triple

Examples:
Enter an integer=>3
Enter an integer=>5
Enter an integer=>4
3,4,5 form a Pythagorean triple

Enter an integer=>5
Enter an integer=>4
Enter an integer=>2
2,4,5 do not form a Pythagorean triple
"""

num1 = int(input("Enter an integer=>"))
num2 = int(input("Enter an integer=>"))
num3 = int(input("Enter an integer=>"))

if (num1 > num2) and (num1 > num3):
    if num1**2 == (num2**2 + num3**2):
        print(str(num1) + "," + str(num2) + "," + str(num3) + " form a Pythagorean triple")
    else :
        print(str(num1) + "," + str(num2) + "," + str(num3) + " do not form a Pythagorean triple")
elif (num2 > num1) and (num2 > num3):
    if num2**2 == (num1**2 + num3**2):
        print(str(num1) + "," + str(num3) + "," + str(num2) + " form a Pythagorean triple")
    else :
        print(str(num1) + "," + str(num2) + "," + str(num3) + " do not form a Pythagorean triple")
elif (num3 > num1) and (num3 > num2):
    if num3**2 == (num1**2 + num2**2):
        print(str(num1) + "," + str(num2) + "," + str(num3) + " form a Pythagorean triple")
    else :
        print(str(num1) + "," + str(num2) + "," + str(num3) + " do not form a Pythagorean triple")
else :
    print(str(num1) + "," + str(num2) + "," + str(num3) + " do not form a Pythagorean triple")
