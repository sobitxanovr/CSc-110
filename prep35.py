def get_highest_sum(values):
    highest = 0
    for a_list in range(0, len(values)):
        for num in range(0, len(values[a_list]) - 1):
            if values[a_list][num] + values[a_list][num + 1] > highest:
                highest = values[a_list][num] + values[a_list][num + 1]
    return highest
