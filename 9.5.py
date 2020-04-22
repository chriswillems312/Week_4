import turtle

def draw_squares(animal, size) :
    for _ in range(100) :
        animal.speed(6)
        animal.forward(size)
        animal.right(91)
        size += 5


window = turtle.Screen()

alex = turtle.Turtle()
draw_squares(alex, 5)
window.mainloop()