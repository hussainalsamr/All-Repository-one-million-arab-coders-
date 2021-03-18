import turtle


def star(color, sides, length, angle, distance):
    galileo = turtle.Turtle()
    galileo.color(color)  # colorful!
    galileo.width(5)  # visible!
    galileo.speed(0)  # ast!
    galileo.penup()
    galileo.left(angle)  # away from center
    galileo.forward(distance)
    galileo.pendown()
    for side in range(sides):
        galileo.forward(length)
        galileo.left(720 / sides)
    galileo.hideturtle()  # just the star


for angle in [180, 135, 90, 45, -45, 0, 270, 225]:
    star("red", 9, 50, angle, 100)

for angle in [180, 135, 90, 45, -45, 0, 270, 225]:
    star("blue", 9, 30, angle, 60)




