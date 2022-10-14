#
# Author: Rustambek Sobithanov
# Course: CSc 110
# Description: The following lines of codes draw a landscape which includes shapes like
#              3 mountains, the sun, moving birds a grassland, fences and some trees.
#              Also, one of the cool features of the program is that the landscape moves
#              as the mouse moves from side to side and up to down.
#
#
from graphics import graphics
import random


def section_one(gui, color_a, color_b, color_c):
    """
    draws the background, sun and mountains
    :param gui: variable that is bound to extracted graphics codes
    :param color_a: one of RGBs that specifies the coloring of the mountains
    :param color_b: one of RGBs that specifies the coloring of the mountains
    :param color_c: one of RGBs that specifies the coloring of the mountains
    :return: background in deep sky blue color, sun in yellow, and mountains
    random colors
    """
    mouse_x = gui.mouse_x
    mouse_y = gui.mouse_y
    gui.rectangle(-100, -100, 1500, 1500, 'deep sky blue')                    # the background
    gui.ellipse(500 + mouse_x/50, 100 + mouse_y/50, 100, 100, 'yellow')       # the sun

    # the mountains
    gui.triangle(350 + mouse_x/8, 150 + mouse_y/8, 0 + mouse_x/8,
                 700 + mouse_y/8, 700 + mouse_x/8, 700 + mouse_y/8, color_a)
    gui.triangle(150 + mouse_x/8, 200 + mouse_y/8, 700 + mouse_x/8,
                 700 + mouse_y/8, -400 + mouse_x/8, 700 + mouse_y/8, color_b)
    gui.triangle(500 + mouse_x/8, 200 + mouse_y/8, 50 + mouse_x/8,
                 700 + mouse_y/8, 950 + mouse_x/8, 700 + mouse_y/8, color_c)


def section_two(gui):
    """
    draws the grassland, the fences around it and some trees
    :param gui: variable that is bound to extracted graphics codes
    :return: the grassland and fences in green and some trees
    """
    mouse_x = gui.mouse_x
    mouse_y = gui.mouse_y
    gui.rectangle(-100 + mouse_x/10, 500 + mouse_y/10, 1000, 500, 'green3')
    x_coordinate = -100
    while x_coordinate < 1000:
        gui.line(x_coordinate + mouse_x/10, 500 + mouse_y/10,
                 x_coordinate + mouse_x/10, 475 + mouse_y/10, 'green', 5)
        x_coordinate += 10
    # the trees
    gui.rectangle(300 + mouse_x/10, 500 + mouse_y/10, 50, 80, 'brown')
    gui.ellipse(325 + mouse_x/10, 435 + mouse_y/10, 90, 160, 'light green')
    gui.rectangle(75 + mouse_x/10, 570 + mouse_y/10, 50, 80, 'brown')
    gui.ellipse(100 + mouse_x/10, 505 + mouse_y/10, 90, 160, 'light green')
    gui.rectangle(600 + mouse_x/10, 520 + mouse_y/10, 50, 80, 'brown')
    gui.ellipse(625 + mouse_x/10, 455 + mouse_y/10, 90, 160, 'light green')


def birds(gui, point_x, point_y):
    """
    draws some birds moving around the screen
    :param gui: variable that is bound to extracted graphics codes
    :param point_x: specifies the x-coordinate of the birds
    :param point_y: specifies the y-coordinate of the birds
    :return: birds moving around the screen infinitely
    """
    gui.line(point_x, point_y, point_x - 15, point_y - 15)
    gui.line(point_x, point_y, point_x + 15, point_y - 15)
    gui.line(point_x + 30, point_y + 20, point_x + 15, point_y + 5)
    gui.line(point_x + 30, point_y + 20, point_x + 45, point_y + 5)
    gui.line(point_x + 60, point_y + 40, point_x + 45, point_y + 25)
    gui.line(point_x + 60, point_y + 40, point_x + 75, point_y + 25)
    gui.line(point_x + 90, point_y + 20, point_x + 75, point_y + 5)
    gui.line(point_x + 90, point_y + 20, point_x + 105, point_y + 5)
    gui.line(point_x + 90, point_y + 60, point_x + 75, point_y + 45)
    gui.line(point_x + 90, point_y + 60, point_x + 105, point_y + 45)


def random_colors(gui):
    """
    picks random colors for the mountains
    :param gui: variable that is bound to extracted graphics codes
    :return: random colors for the mountains each time run
    """
    color_1 = random.randint(0, 255)
    color_2 = random.randint(0, 255)
    color_3 = random.randint(0, 255)
    color_a = gui.get_color_string(color_1, color_2, color_3)
    color_b = gui.get_color_string(color_2, color_3, color_1)
    color_c = gui.get_color_string(color_3, color_1, color_2)
    return color_a, color_b, color_c


def main():
    gui = graphics(700, 700, 'The view')
    point_x = -200
    point_y = 100
    color_a, color_b, color_c = random_colors(gui)
    while True:
        gui.clear()
        if point_x > 700:
            point_x = -200
        section_one(gui, color_a, color_b, color_c)
        section_two(gui)
        birds(gui, point_x, point_y)
        gui.update_frame(30)
        point_x += 5


main()
