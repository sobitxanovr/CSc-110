def get_highest_neighbor(values, row, column):
    back_row = row - 1
    front_row = row + 1
    back_column = column - 1
    front_column = column + 1
    a_list = [values[back_row][column], values[front_row][column],
              values[row][back_column], values[row][front_column]]
    return max(a_list)
