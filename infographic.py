#
# Author: Rustambek Sobithanov
# Course: CSc 110
# Description: The following program reads in a text file and produces an infographic based on
#              its content. It uses the combination of lists, dictionaries, and graphics module
#              to give us the desired result.
#
from graphics import graphics


def main():
    # getting the file name and reading it in
    gui = graphics(650, 700, "Infographics")
    file_name = input()
    the_file = open(file_name, "r")

    # creating a list and appending each element of the file into the list
    all_words = []
    for line in the_file:
        line = line.strip('\n').split()
        for word in line:
            all_words.append(word)

    count_dict = get_count(all_words)
    categorized_list, most_occurrences = categorize(count_dict)
    capitalization, punctuation = capitalization_punctuation(count_dict)

    # drawing the infographic
    while True:
        infographics_text(gui, file_name, count_dict, most_occurrences)
        categorized_column(gui, all_words, categorized_list)
        capitals_column(gui, capitalization, all_words)
        punctuation_column(gui, punctuation, all_words)
        gui.update_frame(1)


def get_count(all_words):
    """
    the function counts how many occurrences of unique words in a given list
    :param all_words: a list containing all the words of a given text file
    :return: a dictionary - keys and values of which are unique words and their counts
    """
    count_dict = {}
    for word in all_words:
        if word in count_dict:
            count_dict[word] += 1
        else:
            count_dict[word] = 1
    return count_dict


def categorize(count_dict):
    """
    the function counts how many small/medium/large words there are in a given dictionary of
    unique words and saves them in a list. Also, it determines what is the smallest, most medium,
    and largest word in each category and saves the word itself and its count in a list
    :param count_dict: a dictionary - keys and values of which are unique words and their counts
    :return: two lists - the first contains the counts of s/m/l words and the other contains
    the most s/m/l words and their counts
    """
    # variables for counting the number of sm/med/lar words
    small_word = 0
    medium_word = 0
    large_word = 0

    # variables for counting which one of the words in each category occurs the most
    smallest = 0
    most_medium = 0
    largest = 0

    # determining the number of sm/med/lar words and the words that occur the most in each
    # category
    for word, count in count_dict.items():
        if len(word) <= 4:
            small_word += count
            if count > smallest:
                smallest = count
                smallest_word = word
        elif 5 <= len(word) <= 7:
            medium_word += count
            if count > most_medium:
                most_medium = count
                most_medium_word = word
        else:
            large_word += count
            if count > largest:
                largest = count
                largest_word = word
    categorized_list = [small_word, medium_word, large_word]
    most_occurrences = [smallest_word, smallest, most_medium_word, most_medium,
                        largest_word, largest]
    return categorized_list, most_occurrences


def capitalization_punctuation(dict_count):
    """
    the function determines how many capitalized, non-capitalized, punctuated, and non-punctuated
    words there are in a given dictionary of words
    :param dict_count: a dictionary - keys and values of which are unique words and their counts
    :return: two lists - the firs contains punctuated and non-punctuated words, and the other
    contains capitalized and non-capitalized words
    """
    capitalized = 0
    non_capitalized = 0
    punctuated = 0
    non_punctuated = 0
    # calculating the number of cap/non-cap and punc/non-punc words
    for word, count in dict_count.items():
        if word[0].isupper():
            capitalized += count
        else:
            non_capitalized += count
        if word[-1] == ',' or word[-1] == '.' or word[-1] == '!' or word[-1] == '?':
            punctuated += count
        else:
            non_punctuated += count
    punctuation = [punctuated, non_punctuated]
    capitalization = [capitalized, non_capitalized]
    return capitalization, punctuation


def infographics_text(gui, file_name, count_dict, most_occurrences):
    """
    the function writes the lines of text displayed at the top of the canvas
    :param gui: variable referring to the canvas
    :param file_name: a string specifying the name of the input text file
    :param count_dict: a dictionary - keys and values of which are unique words and their counts
    :param most_occurrences: a list containing the most sm/med/lar words and their counts
    """
    total = "Total Unique Words: " + str(len(count_dict))
    count = most_occurrences[0] + ' (' + str(most_occurrences[1]) + 'x) '\
            + most_occurrences[2] + ' (' + str(most_occurrences[3]) + 'x) '\
            + most_occurrences[4] + ' (' + str(most_occurrences[5]) + 'x)'
    gui.rectangle(0, 0, 800, 800, "grey30")
    gui.text(50, 20, file_name, "sky blue", 25)
    gui.text(50, 60, total, "white", 25)
    gui.text(50, 100, "Most used words (s/m/l):", "white", 20)
    gui.text(280, 100, count, "sky blue", 20)


def categorized_column(gui, all_words, categorized_list):
    """
    the function draws a bar column which displays the proportion of small, medium and, large
    words out of overall number of words
    :param gui: variable referring to the canvas
    :param all_words: a list containing all the words of a given text file
    :param categorized_list: a list containing the counts of sm/med/lar words
    """
    # calculating the heights of words for the display
    small_word_height = int(round(450 / len(all_words) * categorized_list[0]))
    medium_word_height = int(round(450 / len(all_words) * categorized_list[1]))
    large_word_height = int(round(450 / len(all_words) * categorized_list[2]))

    # determining where each rectangle for a given word starts
    small_start = 200
    medium_start = 200 + small_word_height
    large_start = 200 + small_word_height + medium_word_height

    # drawing the actual bar
    gui.text(50, 160, "Word lengths", "white", 25)
    gui.rectangle(50, small_start, 150, small_word_height, "deep sky blue")
    gui.text(55, small_start + 5, "small words", "white", 15)
    gui.rectangle(50, medium_start, 150, medium_word_height, "green")
    gui.text(55, medium_start + 5, "medium words", "white", 15)
    gui.rectangle(50, large_start, 150, large_word_height, "deep sky blue")
    gui.text(55, large_start + 5, "large words", "white", 15)


def capitals_column(gui, capitalization, all_words):
    """
    the function draws a bar column which displays the proportion of capitalized and
    non-capitalized words out of overall number of words
    :param gui: variable referring to the canvas
    :param capitalization: a list containing the number of capitalized and non-capitalized words
    :param all_words: a list containing all the words of a given text file
    """
    # calculating the height of the cap/non-cap words and where their columns start
    cap_word_height = int(round(450 / len(all_words) * capitalization[0]))
    non_cap_word_height = int(round(450 / len(all_words) * capitalization[1]))
    cap_start = 200
    non_cap_start = 200 + cap_word_height

    # drawing the actual bar
    gui.text(250, 160, "Cap/Non-Cap", "white", 25)
    gui.rectangle(250, cap_start, 150, cap_word_height, "deep sky blue")
    gui.text(255, cap_start + 5, "Capitalized", "white", 15)
    gui.rectangle(250, non_cap_start, 150, non_cap_word_height, "green")
    gui.text(255, non_cap_start + 5, "Non Capitalized", "white", 15)


def punctuation_column(gui, punctuation, all_words):
    """
    the function draws a bar column which displays the proportion of punctuated and
    non-punctuated words out of overall number of words
    :param gui: variable referring to the canvas
    :param punctuation: a list containing the number of punctuated and non-punctuated words
    :param all_words: a list containing all the words of a given text file
    """
    # calculating the height of the pun/non-pun words and where their columns start
    pun_word_height = int(round(450 / len(all_words) * punctuation[0]))
    non_pun_word_height = int(round(450 / len(all_words) * punctuation[1]))
    pun_start = 200
    non_pun_start = 200 + pun_word_height

    # drawing the actual bar
    gui.text(450, 160, "Punct/Non-Punct", "white", 25)
    gui.rectangle(450, pun_start, 150, pun_word_height, "deep sky blue")
    gui.text(455, pun_start + 5, "Punctuated", "white", 15)
    gui.rectangle(450, non_pun_start, 150, non_pun_word_height, "green")
    gui.text(455, non_pun_start + 5, "Non Punctuated", "white", 15)


main()
