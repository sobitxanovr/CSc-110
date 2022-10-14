def get_gpa(grades):
    gpa = 0
    count = 0
    for key in grades:
        if key == 'cs210' or key == 'cs120' or key == 'cs245':
            gpa += grades[key]
            count += 1
    return gpa / count
