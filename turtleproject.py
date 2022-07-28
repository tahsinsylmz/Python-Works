import turtle as t
import random
tim = t.Turtle()
t.colormode(255)
# for i in range(4):
#     tim.fd(50); tim.lt(80)
#
# for i in range(8):
#     tim.undo()
#
#
# for i in range(50):
#     tim.fd(10)
#     tim.pendown()
#     tim.fd(10)
#     tim.penup()


# colours = ["red", "blue", "green", "black", "yellow", "pink", "orange", "purple", "brown", "grey", "blue", "red", "lavender", "dark green"]
# tim.penup()
# tim.left(90)
# tim.fd(100)
# tim.right(90)
# tim.pendown()
# for i in range(3, 14):
#     tim.color(colours[i])
#     angle = 360/(i)
#     for _ in range(i):
#         tim.right(angle)
#         tim.fd(100)


def random_colour():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    my_colour = (r, g, b)
    return my_colour


tim.speed("fastest")
# tim.pensize(10)


# def angle():
#     tim.color(random_colour())
#     a = random.randint(1, 5)
#     tim.right(90*a)
#     tim.fd(50)
#
#
# for i in range(250):
#     angle()


def circle_angle():
    for i in range(180):
        tim.color(random_colour())
        tim.circle(100)
        tim.right(2)


circle_angle()

screen = t.Screen()
screen.exitonclick()
