def count_characters(the_string, character_1, character_2):
    index = 0
    the_sum = 0
    while index < len(the_string):
        if the_string[index] == character_1 or the_string[index] == character_2:
            the_sum += 1
        index += 1
    print("'" + character_1 + "'", "and", "'" + character_2 + "'", "appeared", the_sum,
          "times in the", "string", "'" + the_string + "'")
