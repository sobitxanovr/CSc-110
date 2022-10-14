import os

# taking the input from the user
the_input = input("Enter string:\n")

# creating some variables
index = 0
open_parenthesis = 0
closed_parenthesis = 0

# looping through the string and counting the number of open and closed
# parenthesis.
while index < len(the_input):
    if the_input[index] == "(":
        open_parenthesis += 1
    elif the_input[index] == ")":
        closed_parenthesis += 1

    # declaring the parentheses are unbalanced if the number of closed parentheses
    # exceed that of open ones.
    if closed_parenthesis > open_parenthesis:
        print("Parentheses unbalanced")
        os._exit(0)
    index += 1

# comparing the number of open and closed parentheses and determining if they
# are balanced or not.
if open_parenthesis != closed_parenthesis:
    print("Parentheses unbalanced")
else:
    print("Parentheses balanced")
