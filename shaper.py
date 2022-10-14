#
# Author: Rustambek Sobithanov
# Course: CSc 110
# Description: The following lines of codes are used to print out three shapes (house, plumbbob,
#              and hourglass) using the inputs provided by the user (type of the shape,
#              character using which arrows are printed, and an integer which specifies the
#              height of the border).
#

def upward_arrow(character):
    """
    the following codes print out the upward-facing arrow using while loop and the character
    provided by the user.
    :param character: the input which specifies what to use while printing the arrow
    :return: the upward-facing arrow
    """
    index = 0
    count = 1
    space = 5
    while index < 6:
        print(' ' * space + character * count)
        count += 2
        space -= 1
        index += 1


def downward_arrow(character):
    """
    the following codes print out the downward-facing arrow using a while loop and the character
    provided by the user.
    :param character: the input which specifies what to use while printing the arrow
    :return: the downward-facing arrow
    """
    index = 0
    count = 11
    space = 0
    while index < 6:
        print(' ' * space + character * count)
        count -= 2
        space += 1
        index += 1


def border(height):
    """
    the following lines of codes print out a border with a certain height which is
    specified by the user
    :param height: an integer value which specifies the height of the border
    :return: the border with a certain height
    """
    print('|---------|\n' * height, end='')


def main():
    shape = input('Enter shape to display:\n')
    while shape != 'house' and shape != 'plumbbob' and shape != 'hourglass':
        print('Invalid shape')
        shape = input('Enter shape to display:\n')
    character = input('Enter arrow character:\n')
    height = int(input('Enter row-area height:\n'))

    print('')
    if shape == 'house':
        upward_arrow(character)
        border(height)
    elif shape == 'hourglass':
        border(height)
        downward_arrow(character)
        upward_arrow(character)
        border(height)
    else:
        upward_arrow(character)
        border(height)
        downward_arrow(character)


main()
