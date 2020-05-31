
#############################################################
# FILE : shapes.py
# WRITER : dean_hasenaar , hasenaar , 313584401
# EXERCISE : intro2cs ex2 2016-2017
# DESCRIPTION: A program that calculates the area of shapes
# (a circle or a rectangle or a trapezoid).
#############################################################

import math


def circle_area(radius):
    """this function calculates the area of a circle"""
    
    circ_area = (radius**2)*math.pi
    return circ_area
    
    
def rectangle_area(length, width):
    """this function calculates the area of a rectangle"""
    
    rec_area = length*width
    return rec_area


def trapezoid_area(base1, base2, height_of_trapezoid):
    """this function calculates the area of a trapezoid"""
    
    trapez_area = ((base1 + base2) * height_of_trapezoid) / 2
    return trapez_area    


def shape_area():
    """this function calculates the area of shapes 
    (a circle or a rectangle or a trapezoid)"""
    
    num = int(input("Choose shape (1=circle, 2=rectangle, 3=trapezoid): "))
    if num == 1:
        radius = float(input())
        return circle_area(radius)
    elif num == 2:
        length = float(input())
        width = float(input())
        return rectangle_area(length, width)
    elif num == 3:
        base1 = float(input())
        base2 = float(input())
        height = float(input())
        return trapezoid_area(base1, base2, height)
    else:
        return None
