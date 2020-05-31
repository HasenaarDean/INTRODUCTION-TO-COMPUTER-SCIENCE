
#############################################################
# FILE : calculate_mathematical_expression.py
# WRITER : dean_hasenaar , hasenaar , 313584401
# EXERCISE : intro2cs ex2 2016-2017
# DESCRIPTION: A program that calculates the value of
# two numbers (float or int) according to the arithmetic
# operation (+, *, - or /).
#############################################################


def calculate_mathematical_expression(num1, num2, arithmetic_operation):
    """calculates the value of two numbers
    (float or int) according to the arithmetic
    operation (+, *, - or /)"""

    if arithmetic_operation == "+":
        return num1 + num2

    elif arithmetic_operation == "*":
        return num1 * num2

    elif arithmetic_operation == "/":
        if num2 != 0:
            return num1 / num2

        elif num2 == 0:
            return None
            # impossible to divide by 0.

    elif arithmetic_operation == "-":
        return num1 - num2

    else:
        return None
    # impossible to input a different arithmetic operation.


def calculate_from_string(calculate_str):
    """converts string expression to mathematical expression and calculates
    by using calculate_mathematical_expression"""
    split_calculate_str = calculate_str.split(" ")
    split_calculate_str[0] = float(split_calculate_str[0])
    split_calculate_str[2] = float(split_calculate_str[2])
    return calculate_mathematical_expression(split_calculate_str[0],
                                             split_calculate_str[2],
                                             split_calculate_str[1])
