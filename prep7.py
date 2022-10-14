# inputs asking for the drink size and type
drink_size = input("Drink Size:\n")
drink_type = input("Drink type:\n")
print()

# codes determining how many calories the drink contains
if drink_type == "regular":
    if drink_size == "large":
        print("300 calories")
    else:
        print("150 calories")
elif drink_type == "diet":
    if drink_size == "large":
        print("100 calories")
    else:
        print("50 calories")
else:
    print("0 calories")