from turtle import Turtle, Screen
import random

tim = Turtle()
angles = [0, 90, 180, 270]


def pick_angle():
    angle = random.choice(angles)
    tim.setheading(angle)


def turtle_color():
    R = random.random()
    G = random.random()
    B = random.random()
    tim.color(R, G, B)


def random_walk(steps):
    """
    Set how many steps to go
    :param steps: integer
    :return: None
    """
    for step in range(steps):
        tim.pensize(4)
        pick_angle()
        turtle_color()
        tim.speed(0)
        tim.forward(10)


random_walk(1000)

screen = Screen()
screen.exitonclick()
