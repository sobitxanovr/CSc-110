# user input asking for inches
foot = int(input("Number of feet:\n"))

# changing the units from foot to inch, meter and rod
inch = foot * 12
meter = round(foot * 0.3048, 3)
rod = round(foot / 16.5, 1)
print()
# printing the result
print("Inches:", inch)
print("Meter:", meter)
print("Rods:", rod)
