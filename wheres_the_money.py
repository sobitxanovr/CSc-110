#
# Author: Rustambek Sobithanov
# Course: CSc 110
# Description: The following "program" asks the user for several numeric inputs( annual income,
#              monthly rent, bills, weekly food, and travel expenses) and using them prints a
#              table showing how much money is spent for what. Also, the table includes how
#              much tax is paid and how much extra money is left after all those expenses.
#
#
import os
# introductory statement
print("""-----------------------------
----- WHERE'S THE MONEY -----
-----------------------------""")

# asking for the expenditure for each category and checking if the input is a positive integer
income = input("What is your annual salary?\n")
if income.isnumeric() == False:
    print("Must enter positive integer for salary.")
    os._exit(0)
rent = input("How much is your monthly mortgage or rent?\n")
if rent.isnumeric() == False:
    print("Must enter positive integer for mortgage or rent.")
    os._exit(0)
bills = input("What do you spend on bills monthly?\n")
if bills.isnumeric() == False:
    print("Must enter positive integer for bills.")
    os._exit(0)
food = input("What are your weekly grocery/food expenses?\n")
if food.isnumeric() == False:
    print("Must enter positive integer for food.")
    os._exit(0)
travel = input("How much do you spend on travel annually?\n")
if travel.isnumeric() == False:
    print("Must enter positive integer for travel.")
    os._exit(0)

# calculating the yearly expenditure based on the category
yearly_rent = 12 * int(rent)
yearly_bills = 12 * int(bills)
yearly_food = 52 * int(food)

# determining which type of tax to use
if int(income) <= 15000:
    tax = int(income) * 0.1
elif 15000 < int(income) <= 75000:
    tax = int(income) * 0.2
elif 75000 < int(income) <= 200000:
    tax = int(income) * 0.25
else:
    tax = int(income) * 0.3

# setting a maximum tax possible
if tax > 75000:
    tax = 75000

# calculating the extra money left
extra = int(income) - int(yearly_rent) - int(yearly_bills) - int(yearly_food) - int(travel) - int(tax)

# calculating the percentage
rent_percentage = (int(yearly_rent) * 100) / int(income)
bills_percentage = (int(yearly_bills) * 100) / int(income)
food_percentage = (int(yearly_food) * 100) / int(income)
travel_percentage = (int(travel) * 100) / int(income)
tax_percentage = (int(tax) * 100) / int(income)
extra_percentage = (int(extra) * 100) / int(income)

# formatting the numbers
rent_format = format(int(yearly_rent), '10,.2f')
bills_format = format(int(yearly_bills), '10,.2f')
food_format = format(int(yearly_food), '10,.2f')
travel_format = format(int(travel), '10,.2f')
tax_format = format(int(tax), '10,.2f')
extra_format = format(int(extra), '10,.2f')
rent_percentage_format = format(rent_percentage, '5.1f')
bills_percentage_format = format(bills_percentage, '5.1f')
food_percentage_format = format(food_percentage, '5.1f')
travel_percentage_format = format(travel_percentage, '5.1f')
tax_percentage_format = format(tax_percentage, '5.1f')
extra_percentage_format = format(extra_percentage, '5.1f')

max_length = max(int(rent_percentage), int(bills_percentage),
                 int(food_percentage), int(travel_percentage),
                 int(tax_percentage), int(extra_percentage))

length_of_dashes = int(max_length) + 42
# printing the table
print()
print("-" * length_of_dashes)
print("See the financial breakdown below, based on a salary of $" + income)
print("-" * length_of_dashes)
print("| mortgage/rent | $", rent_format, "|", str(rent_percentage_format)
      + "%", "| " + "#" * int(rent_percentage))
print("|         bills | $", bills_format, "|", str(bills_percentage_format)
      + "%", "| " + "#" * int(bills_percentage))
print("|          food | $", food_format, "|", str(food_percentage_format)
      + "%", "| " + "#" * int(food_percentage))
print("|        travel | $", travel_format, "|", str(travel_percentage_format)
      + "%", "| " + "#" * int(travel_percentage))
print("|           tax | $", tax_format, "|", str(tax_percentage_format)
      + "%", "| " + "#" * int(tax_percentage))
print("|         extra | $", extra_format, "|", str(extra_percentage_format)
      + "%", "| " + "#" * int(extra_percentage))
print("-" * length_of_dashes)

# determining if expenditure exceeds the income and/or if the tax reached its maximum
if tax == 75000:
    print(">>> TAX LIMIT REACHED <<<")
if extra < 0:
    print(">>> WARNING: DEFICIT <<<")



