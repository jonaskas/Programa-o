"""
turtle
"""

import turtle
import random

def bar(t, h, size, factor, color):
    t.color("black", color)
    t.begin_fill()
    t.left(90)
    t.forward(h * factor)
    t.write("{:2}".format(h))
    t.right(90)
    t.forward(size)
    t.right(90)
    t.forward(h * factor)
    t.left(90)
    t.end_fill()
    t.color("black", "gray")

def separator(t, size):
    t.forward(size)

window = turtle.Screen()
window.title("Student grades")
window.bgcolor("white")

my_turtle = turtle.Turtle()
my_turtle.color("black", "gray")
my_turtle.pensize(1)
my_turtle.shape("blank")

my_turtle.penup()
my_turtle.setx(-125)
my_turtle.sety(-75)
my_turtle.pendown()

students = [
    ["student 1", random.randint(0, 20), random.randint(0, 20), random.randint(0, 20)],
    ["student 2", random.randint(0, 20), random.randint(0, 20), random.randint(0, 20)],
    ["student 3", random.randint(0, 20), random.randint(0, 20), random.randint(0, 20)],
    ["student 4", random.randint(0, 20), random.randint(0, 20), random.randint(0, 20)]
]

separator(my_turtle, 10)

for student in students:
    #myTurtle.write(student[0,])
    my_turtle.penup()
    my_turtle.sety(my_turtle.position()[1] - 20)
    my_turtle.write(student[0], move=False, align="left", font=("Arial", 8, "normal"))
    my_turtle.sety(my_turtle.position()[1] + 20)
    my_turtle.pendown()
    for i in range(1, 4):
        bar(my_turtle, student[i], 10, 10, "green" if student[i] >= 9.5 else "red")
        separator(my_turtle, 5)
    separator(my_turtle, 10)
window.mainloop()
