def grade_info(parameter):
    maximum = parameter[0]
    minimum = parameter[0]
    overall = 0
    length = 0
    for index in parameter:
        if index > maximum:
            maximum = index
        elif index < minimum:
            minimum = index
        overall += index
        length += 1
    average = overall / length
    return maximum, minimum, average
