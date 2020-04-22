import turtle

t = turtle.Turtle()
t.penup()
t.forward(-100)
t.pendown()

for i in range(5) :
    t.forward(20)
    t.left(90)
    t.forward(20)
    t.left(90)
    t.forward(20)
    t.left(90)
    t.forward(20)
    t.left(90)
    t.penup()
    t.forward(40)
    t.pendown()
