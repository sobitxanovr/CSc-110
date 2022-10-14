def multiply(the_list):
    overall = 1
    for index in len(the_list):
        overall *= the_list[index]
        index += 1
    return overall
