#enumerate - when u want to get the index and the item at the same time

fruits = ["apple", "banana", "cherry"]

for index, fruit in enumerate(fruits):
    print(index, fruit)

#it is basically a for loop that gives you the index and the item at the same time,
#it converts the list into an enumerate object which is basically a list of tuples
#the above is the same as the following:
for index, fruit in [(0,"apple"),(1,"banana"),(2,"cherry")]:
    print(index, fruit)



#using enumerate with a string
for index, letter in enumerate("hello"):
    print(index, letter)


#f-strings - when u want to format the string
name = "aamir"
age = 30
print(f"my name is {name} and i am {age} years old")

#lenth of a string
len("hello")

#to get the last character of a string
"hello"[-1]

#to get the first character of a string
"hello"[0]

#length of a list
len([1,2,3,4,5])
len(fruits)

waiting_list = ["aamir", "ulfat", "hamoud", "ruhi"]
waiting_list.sort()
print(waiting_list)

# to sort the list in reverse order
waiting_list.sort(reverse=True)
print(waiting_list)

#here we are not assigning the sorted list to a variable as the list is 
# is mutable and we are sorting it in place, however in strings we are not 
# able to sort them in place as strings are immutable

for index, item in enumerate(waiting_list):
    row = f"{index+1}.{item.capitalize()}"
    print(row)

