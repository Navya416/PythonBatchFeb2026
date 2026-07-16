#!/usr/bin/python3
"""
Purpose: Temperature Conversions
    - celsius to fahrenheit , or vice versa


user input : 23c
output     : xF

user input : 23F
output     : xC

23c, 23C, 23F, 23f
23C, 23F
23 C
23C
"""
temp = input("Enter temperature (e.g., 23C or 75F): ").strip().replace(" ", "")

# Validate input
if len(temp) < 2:
    print("Invalid input.")

else:
    unit = temp[-1].upper()
    value = temp[:-1]

    if value.replace(".", "", 1).lstrip("+-").isdigit():

        value = float(value)

        if unit == "C":
            fahrenheit = (value * 9 / 5) + 32
            print(f"{value}°C = {fahrenheit:.2f}°F")

        elif unit == "F":
            celsius = (value - 32) * 5 / 9
            print(f"{value}°F = {celsius:.2f}°C")

        else:
            print("Invalid unit. Use C or F.")

    else:
        print("Invalid temperature value.")