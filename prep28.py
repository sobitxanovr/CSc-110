def get_elements(a_dict, integer):
    a_list = []
    for key in a_dict:
        if key[0].isupper() or key[-1].isupper() or a_dict[key] >= integer:
            a_list.append(a_dict[key])
    return a_list

