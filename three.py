#
# Author: Rustambek Sobithanov
# Course: CSc 110
# Description: The following lines of codes draw three shapes (triangle, rectangle and an ellipse),
#              using a while loop. The drawings are "animated", meaning they move from the left to
#              the right and this loop lasts infinitely. Each time the loop repeats, the points
#              on the y-axis of the shapes change randomly.
#
#
from graphics import graphics
import random


def main():
    x_axis = -50
    gui = graphics(700, 700, 'Canvas')
    y_axis_rectangle = random.randint(50, 650)
    y_axis_ellipse = random.randint(50, 650)
    y_axis_triangle = random.randint(50, 650)
    while True:
        gui.clear()
        gui.rectangle(x_axis - 50, y_axis_rectangle, 100, 100, "red")
        gui.ellipse(x_axis, y_axis_ellipse, 100, 100, "blue")
        gui.triangle(x_axis, y_axis_triangle, x_axis - 50, y_axis_triangle + 100,
                     x_axis + 50, y_axis_triangle + 100, "green")
        if x_axis < 760:
            x_axis += 10
        else:
            x_axis = -50
            y_axis_rectangle = random.randint(50, 650)
            y_axis_ellipse = random.randint(50, 650)
            y_axis_triangle = random.randint(50, 650)
        gui.update_frame(70)


main()
