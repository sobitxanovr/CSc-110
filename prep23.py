def every_other(a_string):
    result = ''
    new_list = a_string.split(' ')
    for index in range(0, len(new_list), 2):
        result += new_list[index] + ' '
    return result
