#
# Author: Rustambek Sobithanov
# Course: CSc 110
# Description: The following lines of codes take a file and encrypt its content by swapping
#              the position lines of the given content. The encrypted file is stored in a
#              new file and as a key its original line indexes are written to another file
#              for a later use.
#
#
import random


def encryption(file):
    """
    takes the file and appends it into a new list. Then, it goes on to use another for-loop
    to swap the places of the elements in the newly-made list
    :param file: a file with a content that needs to be encrypted
    :return: two lists, one of which contains elements in the encrypted format and the other
    contains index keys which can later be used to decrypt the content
    """
    file_info = []
    indexing = []
    index = 1

    # goes over each line of the file removes the new-line character and appends it to a list
    # then in this same list, we create a new list for index keys
    for line in file:
        line = line.strip('\n')
        file_info.append(line)
        indexing.append(index)
        index += 1

    # swaps places of both keys and given file content inside their own lists
    for line_number in range(0, len(file_info) * 5):
        index_1 = random.randint(0, len(file_info) - 1)
        index_2 = random.randint(0, len(file_info) - 1)
        file_info[index_1], file_info[index_2] = file_info[index_2], file_info[index_1]
        indexing[index_1], indexing[index_2] = indexing[index_2], indexing[index_1]
    return file_info, indexing


def main():
    random.seed(125)
    file_name = input('Enter a name of a text file to encrypt:\n')
    file = open(file_name, 'r')
    resulting_file = open('encrypted.txt', 'w')
    file_index = open('index.txt', 'w')
    file_info, indexing = encryption(file)
    for item in file_info:
        resulting_file.write(item + '\n')
    for index in indexing:
        file_index.write(str(index) + '\n')
    resulting_file.close()
    file_index.close()


main()


