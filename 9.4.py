import turtle

def draw_squares(animal, size) :
    for _ in range(18) :
        animal.speed(8)
        animal.forward(size)
        animal.left(90)
        animal.forward(size)
        animal.left(90)
        animal.forward(size)
        animal.left(90)
        animal.forward(size)
        animal.left(90)
        animal.right(20)


window = turtle.Screen()

tess = turtle.Turtle()
draw_squares(tess, 50)

window.mainloop()