#############################################################
# FILE : hello_turtle.py
# WRITER : Dean Hasenaar , hasenaar , 313584401
# EXERCISE : intro2cs ex1 2016-2017
# DESCRIPTION: A simple program that draw 3 flowers by using
# the turtle module.
#############################################################


import turtle


def draw_petal():
    """this function draws one petal."""
    turtle.forward(30)
    turtle.left(45)
    turtle.forward(30)
    turtle.left(135)
    turtle.forward(30)
    turtle.left(45)
    turtle.forward(30)
    turtle.left(135)


def draw_flower():
    """this function draws one flower."""
    turtle.right(45)
    draw_petal()
    turtle.right(90)
    draw_petal()
    turtle.right(90)
    draw_petal()
    turtle.right(90)
    draw_petal()
    turtle.right(135)
    turtle.forward(150)


def draw_flower_advanced():
    """this function draws an advanced flower."""
    draw_flower()
    turtle.left(90)
    turtle.up()
    turtle.forward(150)
    turtle.left(90)
    turtle.forward(150)
    turtle.right(90)
    turtle.down()


def draw_flower_bed():
    """this function draws a flower bed."""
    turtle.up()
    turtle.left(180)
    turtle.forward(200)
    turtle.right(180)
    turtle.down()
    draw_flower_advanced()
    draw_flower_advanced()
    draw_flower_advanced()

draw_flower_bed()
turtle.done()
