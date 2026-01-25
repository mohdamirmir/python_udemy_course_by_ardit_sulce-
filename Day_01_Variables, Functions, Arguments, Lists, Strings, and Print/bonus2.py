x = 1

while x <= 6:
    print(x)
    x = x + 1

prompt = "what is your name? "
name = input(prompt)

while True:
    print(name.capitalize())


prompt1 = "what is your name? "


while True:
    name = input(prompt1)
    print(name.capitalize())

countries = []

while True:
    country = input("Enter the country: ")
    countries.append(country)
    print(countries)