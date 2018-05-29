"""
turtle
"""

import turtle
import random

colors = ["blue", "black", "brown", "red", "orange", "green",
          "yellow", "beige", "turquoise", "pink"]

wn = turtle.Screen()

turtles = [turtle.Turtle() for _ in range(10)]

for i, t in enumerate(turtles):
    t.shape("turtle")
    t.color(colors[i])
    t.penup()
    t.goto(-260, i * 30)
    t.pendown()

for _ in range(100):
    for _, t in enumerate(turtles):
        t.forward(random.randint(0, 10))

wn.listen()
wn.mainloop()
