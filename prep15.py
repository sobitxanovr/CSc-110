def get_height_category(gender, height):
    if gender == 'male':
        if height > 70:
            return 'above average'
        else:
            return 'below average'
    elif gender == 'female':
        if height > 64:
            return 'above average'
        else:
            return 'below average'
    else:
        return 'unknown average'
