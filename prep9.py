# an input asking for a positive integer
the_number = int(input("Enter factorial to calculate:\n"))
print()

# code calculating the factorial of the input
index = 1
the_sum = 1
while index <= the_number:
    the_sum *= index
    index += 1
print(the_number, "factorial =", the_sum)
