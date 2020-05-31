
#############################################################
# FILE : quadratic_equation.py
# WRITER : dean_hasenaar , hasenaar , 313584401
# EXERCISE : intro2cs ex2 2016-2017
# DESCRIPTION: A program that solves a quadratic equation.
#############################################################

import math


def quadratic_equation(a, b, c):
    """This function solves a quadratic equation"""

    # delta is the determinant in the quadratic equation and a, b and c are
    # the parameters
    delta = ((b**2)-(4*a*c))
    result1 = (-b+delta**(1/2))/(2*a)
    result2 = (-b-delta**(1/2))/(2*a)
    if delta > 0:
        return result1, result2
    elif delta == 0:
        return result1, None
    else: 
        return None, None
        

def quadratic_equation_user_input():
    """This function gets 3 inputs of numbers from the user and
    solves a quadratic equation and also tells how many solutions exist
    any try"""

    string = input('Insert coefficients a, b, and c: ') 
    split_string = string.split(" ")
    split_string[0] = float(split_string[0])
    split_string[1] = float(split_string[1])
    split_string[2] = float(split_string[2])
    result1, result2 = \
        quadratic_equation(split_string[0], split_string[1], split_string[2])
    if result2 is not None:
        print("The equation has 2 solutions: " + str(result1) + " and "
              + str(result2))
    elif (result1 is not None) and (result2 is None):
        print("The equation has 1 solution: " + str(result1))
    else:
        print("The equation has no solutions")
