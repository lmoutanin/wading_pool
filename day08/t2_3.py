

import turtle



def polygeon(n,l):
    t = turtle.Turtle()
    for _ in range(n):
        turtle.forward(l)
        turtle.right(360 / n)
    turtle.exitonclick()




polygeon(6,150)