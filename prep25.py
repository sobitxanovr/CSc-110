def count_calories(food):
    calories = 0
    for food_name in food:
        calories += food[food_name]
    return calories
