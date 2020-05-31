
#############################################################
# FILE : largest_and_smallest.py
# WRITER : dean_hasenaar , hasenaar , 313584401
# EXERCISE : intro2cs ex2 2016-2017
# DESCRIPTION: A program that shows the max number and min 
# number from three numbers.
#############################################################


def largest_and_smallest(num1, num2, num3):
    """This function returns the max number
    and min number from three numbers"""

    if num1 > num2:
        if num2 > num3:
            max_val = num1
            min_val = num3
        else: 
            max_val = num1
            min_val = num2
    elif num2 > num3:
        max_val = num2
        if num3 > num1:
            min_val = num1
        else:
            min_val = num3
    else:
        max_val = num3
        min_val = num1
    return max_val, min_val
