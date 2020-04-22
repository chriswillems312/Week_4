import turtle

def draw_squares(animal, size) :
    for _ in range(5) :
        animal.forward(size)
        animal.right(144)
    animal.penup()
    animal.forward(350)
    animal.right(144)
    animal.pendown()

window = turtle.Screen()

alex = turtle.Turtle()
alex.penup()
alex.forward(-50)
alex.pendown()
alex.forward(-150)
for _ in range(5) :
    draw_squares(alex, 50)

window.mainloop()