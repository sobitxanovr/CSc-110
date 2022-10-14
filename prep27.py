def copy_and_increment(a_list):
    copied_version = []
    for item in a_list:
        item = item + 1
        copied_version.append(item)
    return copied_version
