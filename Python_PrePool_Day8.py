"""
    Clément BADRONE
    Last Update 18/09/2024
    EPITECH Pre-Pool PreMSC
"""

import pyjokes
import turtle
import random

def Task_1_1():
    """Say a joke"""
    print(pyjokes.get_joke())

#Task_1_1()

def Task_2_1():
    """Write a program that use this package to draw a square."""
    window = turtle.Screen()
    window.title("Task_2_1")

    pen = turtle.Turtle()
    pen.speed(1)

    pen.pendown()
    pen.goto(0, 50)
    pen.goto(50,50)
    pen.goto(50,0)
    pen.goto(0,0)

#Task_2_1()

def Task_2_2():
    """Can you explain precisely the following snippet of code? Which drawing will you see?"""

    # Create a new window
    toto = turtle . Screen ()
    # Set the background in black
    toto.bgcolor ("black")
    # Create a 'pen'
    titi = turtle . Turtle ()
    # Color of the 'pen' will be red
    titi.color ("red")

    # Draw three circles inside them
    for i in range (3) :
        titi.right (90)
        titi.circle (42)
    # Exit
    toto.exitonclick ()

#Task_2_2()

def Task_2_3():
    """Using turtle, write a function draw_polygon(sides) that takes an integer parameter sides.
    The function draws a regular polygon with the given number of sides"""

    def draw_polygons(sides):
        if sides < 3:
            print(f"Un polygone doit avoir au moins 3 côtés !")
            return
        
        window = turtle.Screen()
        pen = turtle.Turtle()
        pen.speed(3)

        angle = 360 / sides

        for _ in range(sides):
            pen.forward(50)
            pen.left(angle)

    draw_polygons(9)

#Task_2_3()

def Task_2_4():
    """Using turtle, write a program to draw a spiral."""

    window = turtle.Screen()
    pen = turtle.Turtle()
    pen.speed(6)

    for i in range(300):
        pen.circle(i, 20)

#Task_2_4()

def Challenge_Batman():
    """Using turtle and as few lines of code as possible, reproduce one (or more) of the following images."""

    window = turtle.Screen()
    window.bgcolor("black")
    window.title("BATMAN")

    pen = turtle.Turtle()
    pen.color("yellow")
    pen.begin_fill()

    pen.left(90)   
    pen.circle(50, 85)
    pen.circle(15, 110)
    pen.right(180) 

    pen.circle(30, 150)
    pen.right(5)
    pen.forward(10) 

    pen.right(90)
    pen.circle(-70, 140)
    pen.forward(40)
    pen.right(110)

    pen.circle(100, 30)
    pen.circle(30, 100)
    pen.left(50)
    pen.forward(50)
    pen.right(145)

    pen.forward(30)
    pen.left(55)
    pen.forward(10)
    #
    pen.forward(10)
    pen.left(55)
    pen.forward(30)

    pen.right(145)
    pen.forward(50)
    pen.left(50)
    pen.circle(30, 100)
    pen.circle(100, 30)

    pen.right(90)
    pen.right(20)
    pen.forward(40)
    pen.circle(-70, 140)

    pen.right(90)
    pen.forward(10)
    pen.right(5)
    pen.circle(30, 150)

    pen.left(180)
    pen.circle(15, 110)
    pen.circle(50, 85)

    pen.end_fill()

    turtle.done()

#Challenge_Batman()

def Challenge_Spiro():
    """Using turtle and as few lines of code as possible, reproduce one (or more) of the following images."""

    pen = turtle.Turtle()
    pen.speed(0)
    pen.color("purple")
    
    for _ in range(int(360 / 10)):
        pen.circle(100)
        pen.left(100)

    turtle.done()

#Challenge_Spiro()

def Challenge_Multicolor(size, rotations):
    """Using turtle and as few lines of code as possible, reproduce one (or more) of the following images."""

    t = turtle.Turtle()
    t.speed(0)
    colors = ["red", "blue", "green", "yellow", "purple", "orange", "pink", "cyan"]

    for i in range(rotations):
        t.color(random.choice(colors))
        for _ in range(12):
            t.forward(size)
            t.left(30)
        t.left(15)

    turtle.done()

#Challenge_Multicolor(100, 24)

def Draw_Snowflake(length, depth):
    if depth == 0:
        turtle.forward(length)
    else:
        length /= 3
        Draw_Snowflake(length, depth-1)
        turtle.left(60)
        Draw_Snowflake(length, depth-1)
        turtle.right(120)
        Draw_Snowflake(length, depth-1)
        turtle.left(60)
        Draw_Snowflake(length, depth-1)

def Challenge_Snowflake(size, depth):
    """Using turtle and as few lines of code as possible, reproduce one (or more) of the following images."""

    for _ in range(3):
        Draw_Snowflake(size, depth)
        turtle.right(120)

turtle.speed(0)
#Challenge_Snowflake(300, 4)