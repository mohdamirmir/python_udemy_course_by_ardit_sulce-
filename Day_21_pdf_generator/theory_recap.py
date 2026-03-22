#Revision of Python Basics:
#Objects and Variables:

#objects can be stored in variables
from operator import imod
from tkinter import SW


name = "aamir"
last_name = "mir"
id = "1785"

members = 5
height = 1.75
is_male = True

#objects can be produced by functions
name = input("Enter your name: ")
height = float(input("Enter your height: "))

#converting objects to different types
weight = float(input("Enter your weight: "))


#not all functions return a value
x = print("hello")

#custom functions can also return or not return a value
def foo():
    value = 10
    return value

x = foo()
print(x)


def bar():
    print("hello")

x = bar()
print(x)

# Return vs print:
#return is used to return a value from a function howver print is used to print a value to the console


#function with parameters/arguments


def square(number):
    result = number * number
    return result

x=square(2)
print(x)


#function with argument name
x = square(number=2)
print(x)

#without argument name
x = square(2)
print(x)

#functions with multiple arguments
def multiply(number1, number2):
    result = number1 * number2
    return result

x = multiply(number1=2, number2=3) #order of arguments should be respected if not using parameter name
print(x)


#methods
#methods are functions that are associated with an object, they can be called on an object or the variable that 
# holds an object
"this is a string".capitalize()
"this is a string".title()

name = "aamir"
name.capitalize()
name.title()
name.upper()

#methods that return an output
greetings="hello"
greetings.title()

#methods that do not return an output
groceries=["apple","banana","cherry"]
groceries.append("orange")
groceries.remove("banana")
groceries.sort()

#methods modify the object if the object is mutable
groceries=["apple","banana","cherry"]
groceries.append("orange")
print(groceries)

groceries.sort()
print(groceries)

#strings are immutable - once created, they cannot be changed

greetings="hello"
greetings_new=greetings.capitalize()

#to get the methods of an object or instance we use dir() function
dir(int)
dir(float)
dir(str)
dir(list)
dir(dict)
dir(tuple)

dir(greetings)
dir(groceries)

#lists  are mutable - once created, they can be changed
#list is a collection of items that are ordered and mutable
groceries=["apple","banana","cherry"]

#tuples are immutable - once created, they cannot be changed
#tuple is a collection of items that are ordered and immutable
values=("apple","banana","cherry")
#like strings. tuples have no methods to modify them once created
values.append()

#indexing

print(groceries[0]) #first item
print(groceries[2]) #third item
print(groceries[-1]) #last item
print(groceries[-2]) #second last item

string="vinegar"
print(string[0]) #first character
print(string[2]) #third character
print(string[-1]) #last character
print(string[-2]) #second last character

#slicing
groceries[0:2] #first two items
groceries[1:3] #second and third items
groceries[-2:] #last two items
groceries[:2] #first two items
groceries[:-2] #all items except last two
groceries[::2] #every other item
groceries[::-1] #reverse the list

groceries[-3:-1] #third last and second last item


#dictionary
#dictionary is a collection of key-value pairs
#key-value pairs are unordered and mutable
#keys are unique and immutable
#values are not unique and mutable
#keys are used to access the values
#values are used to store the data
#keys are used to access the data
#values are used to store the data

john = {"first_name":"john", last_name:"doe", "age":30}

persons =[{"first_name":"john", "last_name":"doe", "age":30}, 
          {"first_name":"jane", "last_name":"smith", "age":25},
          {"first_name":"jim", "last_name":"beam", "age":35}]

persons2 ={"first_name": ["john", "jane", "jim"], 
            "last_name": ["doe", "smith", "beam"], 
            "age": [30, 25, 35]}

john["first_name"] #access the value of the key "first_name"
persons[1]["first_name"] #access the value of the key "first_name" of the second person
persons2["first_name"][2] #access the value of the key "first_name" of the third person

#while loop
while True:
    password = input("Enter the password: ")

"""
while password != "pass123":
    password = input("Enter the password: ")
    print("Password was incorrect !")
print("Password was correct !")
"""

#for loop
users = ["john", "jane", "jim"]
for user in users:
    print(user.capitalize())


for index, user in enumerate(users):
    print(index, user.capitalize())

#match case 

username = input("Enter the username: ")

match username:
    case "john":
        print("Hello Admin")
    case "jane":
        print("Hello User")
    case "jim":
        print("Hello Guest")
    case _:
        print("Invalid username")


#if-elif-else
if username == "john":
    print("Hello Admin")
elif username == "jane":
    print("Hello User")
elif username == "jim":
    print("Hello Guest")
else:
    print("Invalid username")

#f-strings
name = "aamir"
age = 30
print(f"my name is {name.capitalize()} and i am {age} years old")

#external files

#writing to a file
with open("book.txt", "w") as file:
    file.write("hello")

content="""Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt 
ut labore et dolore magna aliqua. Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium 
doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae"""

#this will overwrite the file with the new content
with open("book.txt", "w") as file:
    file.write(content)


with open("weather.txt", "w") as file:
    file.writelines(["sunny\n", "rainy\n", "cloudy\n"])

#reading from a file
with open("book.txt", "r") as file:
    content = file.read()
print(content)

with open("weather.txt", "r") as file:
    content = file.readlines()
print(content)

clean_content = [item.strip('\n') for item in content]
print(clean_content)



#error handling

#syntax error
#correct code would be to have a closing parenthesis here  ]
clean_content = [item.strip('\n') for item in content)

#here comma is used instead of dot to access the strip method
clean_content = [item,strip('\n') for item in content]

#syntax is correct but apple variable is not defined
clean_content = [item.strip('\n') for item in apple]

#attribute error - there is no steap method in the string class
clean_content = [item.streap('\n') for item in apple]


#value error - there is no int method in the string class
year_of_birth = input("Enter your year of birth: ")
age = 2026 - year_of_birth
print(age)

#fixed code
year_of_birth = input("Enter your year of birth: ")
age = 2026 - int(year_of_birth)
print(age)


#try-except block
try:
    year_of_birth = input("Enter your year of birth: ")
    age = 2026 - int(year_of_birth)
    print(age)
except ValueError:
    print("Enter a valid year of birth")

#try-except-else block
current_year = 2026
try:
    year_of_birth = input("Enter your year of birth: ")
    age = current_year - int(year_of_birth)
    print(age)

except ValueError:
    print("the format should be YYYY")


#docstrings are used to document the code

def area(width, length):
    """
    This function calculates the area of a rectangle
    """
    return width * length

#call the function
print(area(10, 20))


#module is a  python file that contains a collection of functions and can be imported into another python file
import math
print(math.sqrt(16))

#standard library is a collection of modules that are included with Python
import requests
import glob

response = requests.get("https://www.google.com")
content = response.text
print(content)


#web apps need third party libraries also known as frameworks eg streamlit, flask, django, fastapi, etc
import streamlit as st

#desktop gui apps need third party libraries such as pysimplegui, tkinter, etc
import PySimpleGUI as sg


#computers in the past did not have a graphical user interface, they were used to write code and run it.
# all they had was a command line interface (CLI) which is a text based interface where you type commands and get output.
#


#terminal is a text based interface where you type commands and get output.
#pwd is a command to print the current working directory
#pwd

#to create a new file
#touch filename.txt

#to list files in the current directory
#ls
#to list only text files 
#ls *.txt

#create a new directory
#mkdir data 

#to change the new directory
#cd data

#to go back to the previous directory
#cd ..

#remove a file
#rm filename.txt

#remove a directory
#rm -r data

#rename a file
#mv filename.txt newfilename.txt

#copy a file
#cp filename.txt newfilename.txt

#edit a file from the terminal we use nano editor or vim editor
#nano filename.txt
#vim filename.txt




#git
#git is a distributed version control system that is used to track changes in a project.



