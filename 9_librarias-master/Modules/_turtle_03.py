"""
turtle
"""

import turtle

wn = turtle.Screen()
wn.title("Turtle 3")
wn.bgcolor("aqua")

my_turtle = turtle.Turtle()
my_turtle.shape("turtle")
my_turtle.color("green", "lightgreen")

myTurtle2 = turtle.Turtle()
myTurtle2.shape("turtle")
myTurtle2.color("green", "green")

current = my_turtle

def swap():
    global current
    current = myTurtle2 if current == my_turtle else my_turtle

def up():
    current.forward(30)
def left():
    current.left(45)
def right():
    current.right(45)
def down():
    current.backward(30)

def quit():
    wn.bye()

def goto(x, y):
    my_turtle.goto(x, y)
    #wn.title("Turtle at {0}, {1}".format(x, y))

wn.onkey(swap, "s")
wn.onkey(up, "Up")
wn.onkey(left, "Left")
wn.onkey(right, "Right")
wn.onkey(down, "Down")
wn.onkey(quit, "q")
wn.onclick(goto)

wn.listen()
wn.mainloop()
