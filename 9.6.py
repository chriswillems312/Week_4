import turtle
screen = turtle.Screen()
tess = turtle.Turtle()

def draw_poly(draw_turtle, number_of_sides, size):
    angle = 360 / number_of_sides
    for _ in range(number_of_sides):
        draw_turtle.forward(size)
        draw_turtle.left(angle)


def draw_equitriangle(draw_turtle, size):
    draw_poly(draw_turtle, 8, size)

for _ in range(20):
    draw_equitriangle(tess, 100)
    tess.left(360 / 20)

screen.exitonclick()
