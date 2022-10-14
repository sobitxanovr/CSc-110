#
# Author: Rustambek Sobithanov
# Course: CSc 110
# Description: The following lines of codes simulate a game called Reversi, but only in 1-D
#              format. There can be two players and at the beginning of the game they each get
#              half of the board which has the length 12. The players play the game by placing
#              'X' and 'O'. There is a rule which says if either 'X' or 'O' is surrounded by the
#              opposite character, then all the character in the middle flips to the one that it
#              is surrounded with. At the end of the game, the player with more of his characters
#              on the board wins. If the number of both characters match, then it is a Tie.
#

from graphics import graphics

# Some constants to be used throughout the code
# The literals 'X' and 'O' and ' ' should not be used elsewhere
WHITE = 'O'
BLACK = 'X'
EMPTY = ' '


def is_move_acceptable(board, turn, pos):
    """
    the function checks if the position that a player chose is valid or not (i.e. if that
    position is empty or if it is not out of range). It uses if-statements to do so.
    :param board: a list of 12 elements which are either empty string or 'X' or 'O'.
    :param turn: a string that specifies whose turn it is.
    :param pos: an integer showing the position that a player chose to move.
    :return: a boolean value of True if the position is empty, False otherwise.
    """
    if pos not in range(1, 13):
        return False
    elif board[pos - 1] == BLACK or board[pos - 1] == WHITE:
        return False
    return True


def move(board, turn, pos):
    """
    the function places the character to the chosen position and performs flips if necessary
    :param board: a list of 12 elements which are either empty string or 'X' or 'O'.
    :param turn: a string that specifies whose turn it is.
    :param pos: an integer showing the position that a player chose to move.
    """
    index = pos - 1
    board[index] = turn
    opposite_turn = get_opposite_turn(turn)

    # this loop checks if it is necessary to flip the characters on the right
    i = index + 1
    while i < 12 and board[i] == opposite_turn:
        i += 1
    if i < 12:
        if board[i] == turn:
            i = index + 1
            while board[i] != turn:
                board[i] = turn
                i += 1

    # this loop checks if it is necessary to flip the characters on the left
    i = index - 1
    while 0 <= i < 12 and board[i] == opposite_turn:
        i -= 1
    if 0 <= i < 12:
        if board[i] == turn:
            i = index - 1
            while board[i] != turn:
                board[i] = turn
                i -= 1


def get_move(turn):
    """
    the function asks the user for a numeric input which specifies the position on board on
    which he/she wants to move
    :param turn: a string that specifies whose turn it is.
    :return: an integer value of the specified position
    """
    the_move = input(turn + ' choose your move:\n')
    while not the_move.isnumeric():
        the_move = input(turn + ' choose your move:\n')
    return int(the_move)


def is_over(board):
    """
    the function checks if there are empty spaces on the board or not. If there are
    no empty spaces, it ends the game.
    :param board: a list of 12 elements which are either empty string or 'X' or 'O'.
    :return: a boolean value of True if there are no empty spaces, False otherwise.
    """
    for item in board:
        if item == EMPTY:
            return False
    return True


def get_opposite_turn(turn):
    """
    the function determines whose turn it is and gives the turn to the other player
    when the first player finishes making his/her move
    :param turn: a string that specifies whose turn it is.
    :return: a string of either BLACK('X') or WHITE('O') depending on whose turn it is
    """
    if turn == BLACK:
        return WHITE
    else:
        return BLACK


def print_board(board):
    """
    the function creates a list of items which are all initially empty, then as the
    game progresses, it stores the moves at a given indexes in the list.
    :param board: a list of 12 elements which are either empty string or 'X' or 'O'.
    """
    print('+-----------------------+')
    # the for loop is there to put a column between each element so that it gives
    # the shape of a square when printed out
    tiles = '|'
    for item in board:
        tiles += (item + '|')
    print(tiles)
    print('+-----------------------+')


def draw_board(board, gui):
    """
    the function draws the board as the game goes on. So, we can get the visual of
    the game as it is played in real time.
    :param board: a list of 12 elements which are either empty string or 'X' or 'O'.
    :param gui: a variable which helps us to retrieve the lines of codes in another
    file named graphics
    """
    gui.text(260, 30, 'REVERSI', 'black', 40)
    coord_x = 45
    coord_y = 100
    index = 0

    # as the loop iterates it draws the tiles of the board and the character on it one by one
    while index < len(board):
        gui.rectangle(coord_x, coord_y, 60, 60, 'blue')

    # I created this if-statements just because after drawing rectangles, at the end, my green
    # rectangle was going over my black rectangle so that the left ending border was not visible.
    # The if-statements check if the loop is printing out the last rectangle and if so, shrink its
    # width so that the black border becomes visible.
        if index == 11:
            gui.rectangle(coord_x + 5, coord_y + 5, 50, 50, 'light green')
            gui.text(coord_x + 18, coord_y + 10, board[index], 'blue', 35)
        else:
            gui.rectangle(coord_x + 5, coord_y + 5, 55, 50, 'light green')
            gui.text(coord_x + 15, coord_y + 10, board[index], 'blue', 35)
        coord_x += 50
        index += 1
    gui.update_frame(1)


def who_is_winner(board):
    """
    the function determines the result of the game using a for loop and some if-statements
    :param board: a list of 12 elements which are either empty string or 'X' or 'O'.
    :return: a string stating the result of the game ('THERE WAS A TIE', 'BLACK WINS',
    'WHITE WINS')
    """
    counting_x = 0
    counting_o = 0

    # the loop counts how many characters are on board for 'X' and 'O'
    for element in board:
        if element == WHITE:
            counting_o += 1
        elif element == BLACK:
            counting_x += 1

    # the conditions compare the numbers for 'X' and 'O' and determine
    # who won the game or if it is TIE.
    if counting_o == counting_x:
        return 'THERE WAS A TIE'
    elif counting_x > counting_o:
        return 'BLACK WINS'
    return 'WHITE WINS'


def main():
    print('WELCOME TO REVERSI')

    gui = graphics(700, 200, 'reversi')

    # Initialize an empty list with 12 slots
    board = [EMPTY] * 12
    # State of whether or not the game is over
    over = False
    # Starting turn (should alternate as gome goes on)
    turn = BLACK

    # Print out the initial board
    print_board(board)
    draw_board(board, gui)

    # Repeatedly process turns until the game should end (every slot filled)
    while not over:
        place_to_move = get_move(turn)
        while not is_move_acceptable(board, turn, place_to_move):
            place_to_move = get_move(turn)
        move(board, turn, place_to_move)

        print_board(board)
        draw_board(board, gui)

        over = is_over(board)
        turn = get_opposite_turn(turn)
    print('GAME OVER')
    print(who_is_winner(board))


main()
