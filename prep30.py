def longest_string(a_list):
    longest = 'a'
    for dictionary in a_list:
        for key in dictionary:
            if len(longest) < len(dictionary[key]):
                longest = dictionary[key]
    return longest
