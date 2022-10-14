#
# Author: Rustambek Sobithanov
# Course: CSc 110
# Description: The following lines of codes print out a target and locations of various
#              hits on the target using the two inputs which are taken from the user.
#              The first input specifies where exactly the hits should be printed out,
#              and the second input specifies what kind of character is used to display
#              the hit(s) on the target.
#

# Accepting the user inputs (location of hits and character of the hits),
# checking if the first input is the multiple of 4 and at least 3 character long
# and checking if the second input is exactly 1 character long
location = input("Hit string:\n")
while len(location) < 4 or len(location) % 4 != 0:
    print("Please provide a valid hit string.")
    location = input("Hit string:\n")
character = input("Marker:\n")
while 0 <= len(character) > 1:
    print("Please provide a valid marker.")
    character = input("Marker:\n")

# printing the target and the hits using nested while-loops
index_row = 5
index_column = -7
count = 4
the_table = ''
current_hit_x = int(location[0] + location[1])
current_hit_y = int(location[2] + location[3])
while index_row >= -5:
    while index_column <= 7:
        if index_column == current_hit_x and index_row == current_hit_y:
            the_table += character
            if count < len(location):
                current_hit_x = int(location[count] + location[count + 1])
                current_hit_y = int(location[count + 2] + location[count + 3])
                count += 4
        elif index_column == 0:
            the_table += '|'
        elif index_row == 0:
            the_table += '-'
        else:
            the_table += ' '
        index_column += 1
    print(the_table)
    index_column = -7
    the_table = ''
    index_row -= 1
