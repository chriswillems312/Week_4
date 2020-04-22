import turtle

def draw_poly(t, n, sz) :
    for _ in range(n) :
        tess.forward(sz)
        tess.left(45)


window = turtle.Screen()

tess = turtle.Turtle()
draw_poly(tess, 8, 50)

window.mainloop()