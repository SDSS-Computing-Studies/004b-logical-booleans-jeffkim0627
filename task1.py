
#! python3
"""
The Earth maintains an orbit where it's closest distance to  
the sun is 0.9759 AU and it's furthest distance to the sun is 
1.016 AU. 
Ask the user to enter a number. 
Tell them if the number is between 0.9759 and 1.016.
(2 points)

Inputs:
a number (float)

Outputs:
That is within normal Earth orbit.
That is not within normal Earth orbit.
"""
number = float(input("Enter a number"))

if 0.9759 <= number <= 1.016:
    print("The number is between 0.9759 and 1.016")
else :
    print("The number is not between 0.9759 and 1.016")