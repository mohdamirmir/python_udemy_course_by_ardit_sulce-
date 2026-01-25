feet_inches = input("Enter feet and inches: ")

def parse(feet_inches):
    parts =  feet_inches.split(" ")
    feet = float(parts[0])
    inches = float(parts[1])
    return feet, inches

def convert(feet, inches):
    meters = feet * 0.3048 + inches * 0.0254
    return meters
    # return f"{feet} feet and {inches} inches is equal to {meters} meters"

feet, inches = parse(feet_inches)
print(feet, inches)
result = convert(feet, inches)

if result < 1:
    print("Kid is too small.")
else:
    print("Kid can use the slide.")



