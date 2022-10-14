###
### Author: Rustambek Sobithanov
### Class: CSc 110
### Description: The following program prints out a tie-fighter. It first asks the user
###              for a numeric input and then adjusts the width of the tie-fighter
###              accordingly.
###
width = int(input('Enter TIE width:\n'))
print()
print("|[" + " " * width + "         " + " " * width + "]|")
print("|[" + " " * width + "         " + " " * width + "]|")
print("|[" + " " * width + "         " + " " * width + "]|")
print("|[" + " " * width + " /=---=\ " + " " * width + "]|")
print("|[" + " " * width + "/==---==\\" + " " * width + "]|")
print("|[" + "/" * width + "|== X ==|" + "\\" * width + "]|")
print("|[" + " " * width + "\==---==/" + " " * width + "]|")
print("|[" + " " * width + " \=---=/ " + " " * width + "]|")
print("|[" + " " * width + "         " + " " * width + "]|")
print("|[" + " " * width + "         " + " " * width + "]|")
print("|[" + " " * width + "         " + " " * width + "]|")
