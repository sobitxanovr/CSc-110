def sum_nums(a_list):
    sums = 0
    for index in a_list:
        for num in index:
            if num < 10:
                sums += num
    return sums
