import turtle as t
from turtle import Turtle, Screen
import random

t.colormode(255)
color_list = [(246, 245, 243), (233, 239, 246), (246, 239, 242), (240, 246, 243), (132, 166, 205), (221, 148, 106),
              (32, 42, 61), (199, 135, 148), (166, 58, 48), (141, 184, 162), (39, 105, 157), (237, 212, 90),
              (150, 59, 66), (216, 82, 71), (168, 29, 33), (235, 165, 157), (51, 111, 90), (35, 61, 55), (156, 33, 31),
              (17, 97, 71), (52, 44, 49), (230, 161, 166), (170, 188, 221), (57, 51, 48), (184, 103, 113),
              (32, 60, 109), (105, 126, 159), (175, 200, 188), (34, 151, 210), (65, 66, 56), (106, 140, 124),
              (153, 202, 227), (48, 69, 71), (131, 128, 121)]
Simon = Turtle()
Simon.speed(0)


def draw_along_line(dot_num):
    for _ in range(dot_num):
        for _ in range(dot_num):
            Simon.dot(20, random.choice(color_list))
            Simon.penup()
            Simon.hideturtle()
            Simon.forward(50)
            Simon.pendown()
        Simon.penup()
        Simon.setheading(180)
        Simon.forward(50 * (dot_num))
        Simon.right(90)
        Simon.forward(50)
        Simon.setheading(0)
    Simon.home()


Simon.setheading(225)
Simon.penup()
Simon.forward(300)
Simon.setheading(0)
Simon.pendown()
draw_along_line(10)

screen = Screen()
screen.exitonclick()
