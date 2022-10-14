def count_vowels(a_string, num_1, num_2):
    counting_vowels = 0
    for index in range(num_1, num_2 + 1):
        if a_string[index] == 'a' or a_string[index] == 'e' or a_string[index] == 'i':
            counting_vowels += 1
        elif a_string[index] == 'o' or a_string[index] == 'u':
            counting_vowels += 1
    return counting_vowels
