def swap(dict_data, set_data):
    a_list = []
    for num in set_data:
        for key in dict_data:
            if num == key:
                a_list.append(key)
    for key in a_list:
        dict_data[dict_data[key]] = key
        del dict_data[key]
    return dict_data
