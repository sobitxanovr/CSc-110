def most_common_vehicle(file_name):

    # first reads through the file and creates a list of amounts included in the file
    # then creates another list including the names of the cars which correspond to
    # the specific amounts in the first list
    a_file = open(file_name, 'r')
    num_list = a_file.readlines()
    vehicle_names = ['Toyota', 'Ford', 'Chevy']

    # identifies if there is a tie or not
    index = 0
    comparing = num_list[2]
    while index < len(num_list):
        if comparing != num_list[index]:
            comparing = num_list[index]
        else:
            return print('There\'s a tie!')
        index += 1

    # finds which one of the cars is the most common
    num = 0
    index = -1
    for element in num_list:
        if num < int(element):
            num = int(element)
            index += 1

    # printing the result
    print(vehicle_names[index], 'most common')
