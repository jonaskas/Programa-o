"""
turtle
"""

import turtle
import random

window = turtle.Screen()
window.bgcolor("lightgreen")
window.title("My first Turtle")
my_turtle = turtle.Turtle()
my_turtle.shape("turtle") # blank, circle, classic, square, triangle, turtle
my_turtle.pensize(2)
my_turtle.speed(5)

def circle():
    my_turtle.pendown()
    my_turtle.color("red")
    my_turtle.begin_fill()
    my_turtle.circle(random.randint(-30, 30))
    my_turtle.end_fill()

for c in range(4):
    circle()
    my_turtle.color("green")
    my_turtle.penup()
    for i in range(10):
        my_turtle.stamp()
        my_turtle.forward(20)
    my_turtle.right(90)

my_turtle.hideturtle()
window.mainloop() # Wait for user input to close window
