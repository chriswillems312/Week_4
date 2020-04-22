import turtle

def draw_squares(animal, size) :
    for _ in range(15) :
        animal.forward(size)
        animal.left(90)
        animal.forward(size)
        animal.left(90)
        animal.forward(size)
        animal.left(90)
        animal.forward(size)
        animal.left(90)
        animal.penup()
        animal.forward(-10)
        animal.right(90)
        animal.forward(10)
        animal.left(90)
        animal.pendown()
        size += 20

window = turtle.Screen()

alex = turtle.Turtle()
draw_squares(alex, 20)
window.mainloop()