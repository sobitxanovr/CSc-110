# inputs asking the food type and the price of the food
food_type = input("Enter food:\n")
price = int(input("Enter price:\n"))

# codes determining if the user given food type is expensive or affordable
if price > 20:
    print("That", food_type, "is expensive.")
else:
    print("That", food_type, "is affordable.")
