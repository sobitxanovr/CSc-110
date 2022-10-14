#
# Author: Rustambek Sobithanov
# Course: CSc 110
# Description: The following program asks a user for a csv file input, column number and what
#              to carry out in the given column. After taking the inputs, the program carries
#              out the given operation (finding the average, minimum, or maximum in the given
#              column). Finally, it prints out the result of the operation.
#
#
def main():
    # asking for the inputs
    file_name = input("Enter CSV file name:\n")
    col_num = input("Enter column number:\n")
    col_oper = input("Enter column operation:\n")

    # creating a 2D list the contents of which are the lines of the given file
    the_file = open(file_name, "r")
    the_list = []
    for line in the_file:
        line = line.strip().split(",")
        the_list.append(line)

    # determining which function to use depending on the operation mode
    if col_oper == 'min':
        result_min = operation_min(the_list, int(col_num))
        print("The minimum value in column", col_num, "is:", result_min)
    elif col_oper == 'max':
        result_max = operation_max(the_list, int(col_num))
        print("The maximum value in column", col_num, "is:", result_max)
    else:
        result_avg = operation_avg(the_list, int(col_num))
        print("The average for column", col_num, "is:", result_avg)


def operation_min(the_list, col_num):
    """
    the function iterates through the 2D list and finds the minimum value at a given
    column
    :param the_list: a 2D list containing float numbers
    :param col_num: an integer specifying the column number in which the operation will
    be carried out
    :return: a float number which is the result of the operation
    """
    result = 99999
    for row in the_list:
        for column in row:
            if row.index(column) == (col_num - 1) and float(result) > float(column):
                result = column
    return result


def operation_max(the_list, col_num):
    """
    the function iterates through the 2D list and finds the maximum value at a given
    column
    :param the_list: a 2D list containing float numbers
    :param col_num: an integer specifying the column number in which the operation will
    be carried out
    :return: a float number which is the result of the operation
    """
    result = 0
    for row in the_list:
        for column in row:
            if row.index(column) == (col_num - 1) and float(result) < float(column):
                result = column
    return result


def operation_avg(the_list, col_num):
    """
    the function iterates through the 2D list and finds the average for a given
    column
    :param the_list: a 2D list containing float numbers
    :param col_num: an integer specifying the column number in which the operation will
    be carried out
    :return: a float number which is the result of the operation
    """
    result = 0
    count = 0
    for row in the_list:
        result += float(row[col_num - 1])
        count += 1
    return result / count


main()
