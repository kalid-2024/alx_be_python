FAHRENHEIT_TO_CELSIUS_FACTOR =5/9
CELSIUS_TO_FAHRENHEIT_FACTOR =9/5

def convert_to_celsius(fahrenheit):
    global FAHRENHEIT_TO_CELSIUS_FACTOR
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    global CELSIUS_TO_FAHRENHEIT_FACTOR
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

try:
    value = float(input("Enter the temperature to convert: "))
except ValueError:
    print("Invalid temprature. Please enter a numeric value.")

unit = input("Is this temperature in Celsius or Fahrenheit? (C/F):")
match unit.upper():
    case 'C':
        print(f"{value}°C is {convert_to_fahrenheit(value)}°F")
    case 'F':
        print(f"{value}°F is {convert_to_celsius(value)}°C")
    case _:
        print("Invalid unit. Please enter 'C' or 'F'.")

