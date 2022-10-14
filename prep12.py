def average_numbers(frequency):
    the_sum = 0
    index = 0
    while index < frequency:
        number = int(input("Number:\n"))
        the_sum += number
        index += 1
    average = round(the_sum / frequency, 2)
    print("Average =", average)
