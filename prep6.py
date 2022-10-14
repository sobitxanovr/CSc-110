# the user input asking for the temperature in fahrenheit
temperature = int(input("Temperature in fahrenheit:\n"))

# codes determining the state of the water depending on the temperature
if 32 < temperature < 212:
    print("Water")
if temperature <= 32:
    print("Ice")
if temperature >= 212:
    print("Steam")
