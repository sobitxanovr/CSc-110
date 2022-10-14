def get_supply_count():
    a_file = open('supplies.txt', 'r')
    total = open('total.txt', 'w')
    elements = a_file.readlines()
    count = 0
    for item in elements:
        item = item.rstrip('\n')
        item = item.split(' ')[1]
        if item.isnumeric():
            count += int(item)
    total.write(str(count))


get_supply_count()
