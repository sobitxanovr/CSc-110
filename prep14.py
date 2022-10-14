def calculate_tree_height(height, years):
    index = 0
    while index < years:
        height *= 1.2
        index += 1
    return round(height, 4)
