def differences(set_1, set_2):
    count = len(set_1 - set_2)
    count += len(set_2 - set_1)
    return count
