#
# Author: Rustambek Sobithanov
# Course: CSc 110
# Description: The following program accepts 3 inputs, and using given inputs the program
#              searches for the hidden words in a word-search grid. The first input is a
#              file which contains words that should be found. The second input is also a
#              a file, but this one contains the word-search grid. The last is a string
#              which specifies how the program should carry out the search - either
#              'horizontally' (h) or 'vertically' (v).
#
def file_to_dictionary(words_file):
    """
    the function converts a given file into a list and then into from the list into a dictionary
    :param words_file: a file containing words that should be found
    :return: a dictionary keys being words that should be found and values the same words but in
    a reversed order
    """
    words = open(words_file, 'r')
    a_dictionary = {}
    a_list = []
    # splits each line into two and adds them into a list as elements
    for line in words:
        line = line.strip().split(' : ')
        a_list.append(line[0])
        a_list.append(line[1])
    index = 0
    # converts the list into a dictionary
    while index < len(a_list):
        a_dictionary[a_list[index]] = a_list[index + 1]
        index += 2
    return a_dictionary


def file_to_list(puzzle_file):
    """
    the function converts a given file into a list
    :param puzzle_file: a file containing word-search grid
    :return: a list the elements of which are lines in a given file
    """
    puzzle = open(puzzle_file, 'r')
    puzzle_list = []
    k = 0
    # removes the '\n', makes all the letters lowercase and joins them together
    # with no space in between and adds them into a list as elements
    for line in puzzle:
        line = line.strip().lower().split(' ')
        puzzle_list.append(line)
        puzzle_list[k] = ''.join(puzzle_list[k])
        k += 1
    return puzzle_list


def horizontal_search(a_dictionary, puzzle_list, mode):
    """
    the function uses some conditionals and nested for loop to search for the hidden words
    horizontally; it also prints out which word is found and its location
    :param a_dictionary: a dictionary which contains words that are searched for
    :param puzzle_list: a list which contains lines of the word-search grid as elements
    :param mode: a string specifying the mode of the search
    """
    column = 1
    # each line in the grid iterates through keys and values of the dictionary and checks if
    # they either the key or value are in the line
    for item in puzzle_list:
        for key in a_dictionary:
            if key in item:
                index = len((item.split(key))[0]) + 1
                # determines how to print the result depending on the mode
                if mode == 'h':
                    print(key, 'found at', '[' + str(column) + ',', str(index) + ']')
                else:
                    print(key, 'found at', '[' + str(index) + ',', str(column) + ']')
            elif a_dictionary[key] in item:
                index = len(item) - len(item.split(a_dictionary[key])[1])
                # determines how to print the result depending on the mode
                if mode == 'h':
                    print(key, 'found at', '[' + str(column) + ',', str(index) + ']')
                else:
                    print(key, 'found at', '[' + str(index) + ',', str(column) + ']')
        column += 1


def vertical_search(a_dictionary, puzzle_list, mode):
    """
    the function uses a for loop and calls another function to search for the hidden words
    vertically; it also prints out which word is found and its location
    :param a_dictionary: a dictionary which contains words that are searched for
    :param puzzle_list: a list which contains lines of the word-search grid as elements
    :param mode: a string specifying the mode of the search
    """
    vertical_line = ''
    vertical_list = []
    # after the end of the loop, the grid will be in a form in which it is rotated 90 degrees
    # clockwise, so that the vertical search becomes horizontal.
    for num in range(0, len(puzzle_list[0])):
        for item in puzzle_list:
            vertical_line += item[num]
        vertical_list.append(vertical_line)
        vertical_line = ''
    horizontal_search(a_dictionary, vertical_list, mode)


def main():
    words_file = input('Enter word file:\n')
    puzzle_file = input('Enter puzzle file:\n')
    search_method = input('Enter puzzle mode:\n')
    a_dictionary = file_to_dictionary(words_file)
    puzzle_list = file_to_list(puzzle_file)
    if search_method == 'h':
        horizontal_search(a_dictionary, puzzle_list, search_method)
    else:
        vertical_search(a_dictionary, puzzle_list, search_method)


main()
