#
# Author: Rustambek Sobithanov
# Course: CSc 110
# Description: The following program reads in data set, and prints out the plot of first digits.
#              Then, it checks if the plot follows the Benford's law or not, and depending on
#              the result of the check, it prints out whether the plot follows the law or not.
#
#
def main():
    # getting the file name and opening it in a read mode
    file_name = input("Data file name:\n")
    a_file = open(file_name, "r")

    # iterating through each line and appending the numeric value to a list
    num_list = []
    for line in a_file:
        line = line.strip().split(",")
        for element in line:
            if element[0].isnumeric() and element[0] != '0' and element[-1].isnumeric:
                num_list.append(float(element))
    print()
    percentage = calculate_and_print(num_list)
    print()
    print(validation(percentage))


def calculate_and_print(num_list):
    """
    the function takes a list as a parameter and counts how many times digits 1-9 occur
    as leading digits in given data. Then, it calculates their percentage and stores
    them in a dictionary. Finally, it prints the plot of first digits according to the
    percentages given.
    :param num_list: a list, the elements of which are float numbers
    :return: a dictionary, the keys of which are digits 1-9 and the values are the
    percentage of how many times the digits occur in the given data
    """
    # counting how many times digits 1-9 occur as leading digits in the data
    count_dict = {}
    for num in num_list:
        if int(str(num)[0]) in count_dict:
            count_dict[int(str(num)[0])] += 1
        else:
            count_dict[int(str(num)[0])] = 1

    # getting the percentage of the frequency of occurrences of some digit in the data
    percentage = {}
    for digit, count in count_dict.items():
        percentage[digit] = int((count / len(num_list)) * 100)

    # printing out the plot according to the identified percentage
    for num in range(1, 10):
        print(num, '|', '#' * percentage[num])
    return percentage


def validation(percentage):
    """
    the function checks if the data of numeric values follows Benford's law or not
    :param percentage:a dictionary, the keys of which are digits 1-9 and the values are the
    percentage of how many times the digits occur in the given data
    :return: a string statement of whether the plot follows Benford's law or not
    """
    # storing the actual requirements for Benford's law to be True in a dictionary
    actual_percentage = {1: 30, 2: 17, 3: 12, 4: 9, 5: 7, 6: 6, 7: 5, 8: 6, 9: 4}

    # comparing the values we got from the data to the actual should-be values
    check = None
    for num in range(1, 10):
        if percentage[num] - 10 < actual_percentage[num] < percentage[num] + 5:
            check = "Follows Benford's Law"
        else:
            return "Does not follow Benford's Law"
    return check


main()
