import turtle
t = turtle.Turtle()
t.color("white")
t.width(1)
t.speed(0)
t.hideturtle()

def square(number):
    return number * number

for n in range(1260):
    angle = square(n)
    t.right(angle + .12)
    t.forward(5)