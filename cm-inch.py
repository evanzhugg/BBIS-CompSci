# cm to inch

cm = int(input("Enter the length in cm: "))
if cm < 0:
    raise ValueError("The length cannot be negative")
else:
    pass

try:
    inch = cm / 2.54
    print(f"The length in inches is {inch}")
except ZeroDivisionError:
    print("The length cannot be zero")
except ValueError:
    print("The input must be a number")

# temperature
def ctof (c):
    f = (c * 9/5) + 32
    return f
def ftoc (f):
    c = (f - 32) * 5/9
    return c
unit = input("Enter the unit of temperature (C/F): ").lower()
if unit == "c":
    c = float(input("Enter the temperature in Celsius: "))
    if c < -273.15:
        raise ValueError("The temperature is below absolute zero")
    elif -273.15 <= c <= 0:
        print("The temperature is below freezing point")
    elif c == 0:
        print("The temperature is at freezing point")
    elif 0 < c < 100:
        print("The temperature is in the normal range")
    elif c == 100:
        print("The temperature is at boiling point")
    elif c > 100:
        print("The temperature is above boiling point")

    f = ctof(c)
    print(f"The temperature in Fahrenheit is {f}")
if unit == 'f':
    f = float(input("Enter the temperature in Fahrenheit: "))
    c = ftoc(f)
    print(f"The temperature in Celsius is {c}")
    if c < -273.15:
        raise ValueError("The temperature is below absolute zero")
    elif -273.15 <= c <= 0:
        print("The temperature is below freezing point")
    elif c == 0:
        print("The temperature is at freezing point")
    elif 0 < c < 100:
        print("The temperature is in the normal range")
    elif c == 100:
        print("The temperature is at boiling point")
    elif c > 100:
        print("The temperature is above boiling point")




