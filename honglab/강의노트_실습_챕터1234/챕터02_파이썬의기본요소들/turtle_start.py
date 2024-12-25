# https://docs.python.org/3/library/turtle.html

import turtle

t = turtle.Turtle()

# turtle.setup(1280, 960)
# turtle.screensize(400, 300)
t.speed("slowest")
t.shape("turtle")
t.turtlesize(2)
t.color("green")
t.pencolor("blue")
t.screen.bgcolor("aqua")

for i in range(4):
    t.forward(200)
    t.left(90)

turtle.done()
