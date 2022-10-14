#
# File: utils.py
# Author: Rustambek Sobithanov
# Description:
#

# Changes to this file should only be inside function definitions

def find_mine(grid, x, y, position):
    """
    Determines if a square from a relative position contains a mine.
    Returns 1 if there is, otherwise returns 0.

    Parameters:
    grid:       2D list containing X's representing bombs and numbers which are
                either the number of adjacent X's or 0.
    x:          Integer which is the x postiion to be scanned for mines.
    y:          Integer which is the y postiion to be scanned for mines.
    position:        A tuple containing the relative coordinates to scan

    Examples:
    grid = [["X", 0],
            [0, "0"]]

    find_mine(grid, 0, 0, (0, 0)))    Returns: 1
    find_mine(grid, 0, 0, (1, 0)))    Returns: 0
    find_mine(grid, 0, 0, (0, 1)))    Returns: 1
    find_mine(grid, 0, 0, (1, 1)))    Returns: 0
    find_mine(grid, 0, 0, (20, 20)))  Returns: 0
    """


def count_total_moves(grid):
    """
    Counts the number of moves that need to be made for the player to
    win the game. (Counts number of squares that are not mines)

    Parameter:
    grid:       2D list containing X's representing mines and numbers which are
                the number of adjacent X's.
    """


def determine_game_status(grid, count):
    """
    Returns a boolean which is True if the game should continue or
    False if the game is over. False is returned if a mine has been
    revealed or count is 0 meaning there are no squares without mines
    that are not revealed.
    Parameter:
    grid:       2D list containing X's representing mines and numbers which are
                the number of adjacent X's.
    count:      Integer which is the number of mineless squares left to be revealed.
    """


def dig(grid, coordinate, user_view):
    """
    Translates an item at a coordinate on the grid to the correspoinding
    location on the user_view.

    Parameters:
    grid:       2D list containing X's representing mines and numbers which are
                the number of adjacent X's.
    coordinate: A string where the first character is the x-position and the
                characters that follow makes up the y-position for where to dig.
                NOTE: The x-position is a letter and the y-position is a number.
    user_view:  2D list containing X's representing mines and numbers which are
                either the number of adjacent X's or 0. Unlike grid, some of the
                values are empty meaning the user has not seen the square.
    """



def update_grid(grid):
    """
    Populates non-mine squares with the number of adjacent mines.
    Basically, iterate through the grid and replace the ' ' strings with
    a string with a number in it, representing how many mines
    neighbor this location.
    Parameters:
    grid:       2D list containing X's representing bombs and numbers which are
                either the number of adjacent X's or 0.
    """
    count = 0
    for row in range(len(grid)):
        for column in range(len(grid[row])):
            if grid[row][column] == 'X':
                grid[row][column] = 'X'
            elif row == 0 and len(grid) > 2 and column == 0:
                if grid[row][column + 1] == 'X':
                    count += 1
                if grid[row + 1][column] == 'X':
                    count += 1
                if grid[row + 1][column + 1] == 'X':
                    count += 1
                grid[row][column] = str(count)



def print_grid(grid):
    """
    Prints out a 2D grid with the y-axis labeled with numbers and the x-axis with letters.

    Parameters:
    grid:       2D list containing X's representing bombs and numbers which are
                the number of adjacent X's.
    """


def make_empty_clone(grid):
    """
    Returns a 2D list which is the same dimensions (rows / columns) as a passed in grid.
    The returned list should contain ' ' strings only
    """
    empty_list = []
    for lists in grid:
        inside_list = []
        for element in lists:
            inside_list.append(' ')
        empty_list.append(inside_list)
    return empty_list
