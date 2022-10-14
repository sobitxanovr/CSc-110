#
# Author: Rustambek Sobithanov
# Course: CSc 110
# Description: The following lines of codes decrypt a file. Both the file and its index keys
#              are provided by the user. After decrypting the given file, it stores its content
#              into another file.
#
#
def decryption(the_file, the_index):
    """
    the function decrypts the given file using the index keys
    :param the_file: a file with encrypted content
    :param the_index: a file with index keys used to decrypt the encrypted file
    :return: a list with decrypted elements from the encrypted file
    """
    new_list = []
    file_list = []
    index = 0

    # goes over each line in the encrypted file, removes the new-line character and
    # appends it to a list. Also, this same loop appends some numbers into a list
    # for a later use
    for line in the_file:
        line = line.strip('\n')
        new_list.append(index)
        index += 1
        file_list.append(line)
    index_list = []

    # goes over each line in the index-keys file, removes the new-line character,
    # converts it to an integer, subtracts one to match the actual indexes in the
    # list and appends it to a list.
    for item in the_index:
        item = item.strip('\n')
        actual_index = int(item) - 1
        index_list.append(actual_index)

    # decrypts the given information in the encrypted file
    for num in range(0, len(index_list)):
        new_list[index_list[num]] = file_list[num]
    return new_list


def main():
    encrypted_file = input('Enter the name of an encrypted text file:\n')
    indexed_file = input('Enter the name of the encryption index file:\n')
    the_file = open(encrypted_file, 'r')
    the_index = open(indexed_file, 'r')
    decrypted_file = open('decrypted.txt', 'w')
    new_list = decryption(the_file, the_index)

    # writes each element into a new file
    for line in new_list:
        decrypted_file.write(str(line) + '\n')
    decrypted_file.close()


main()
