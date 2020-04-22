import turtle
window = turtle.Screen()
alex = turtle.Turtle()

def draw_squares(animal, size) :
    for _ in range(4) :
        animal.forward(size)
        animal.left(90)

    animal.penup()
    animal.forward(40)
    animal.pendown()

for _ in range(5) :
    draw_squares(alex, 20)

window.mainloop()