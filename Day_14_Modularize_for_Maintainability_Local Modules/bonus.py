from parsers import parse
from converters import convert

feet_inches = input("Enter feet and inches: ")

feet, inches = parse(feet_inches)
print(feet, inches)
result = convert(feet, inches)

if result < 1:
    print("Kid is too small.")
else:
    print("Kid can use the slide.")



