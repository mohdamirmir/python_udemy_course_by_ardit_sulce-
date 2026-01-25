mylist = ['a','b','c']

#first and last element in the list
mylist[0]
mylist[-1]

name = "aamir.mir111"
name = name.replace(".","-")
#changing the first occurence of a character in the string
name = name.replace(".","-",1)
print(name)


#to access the element in the list
mylist[0]

#to get the index of an element in the list
mylist.index('b')

#to add an element to the list
mylist.append('d')

#to add an element to the list at a specific index
mylist.insert(0, 'z')

#to remove an element from the list
mylist.remove('b')      

#to clear the list
mylist.clear()

#to sort the list
mylist.sort()

#to reverse the list
mylist.reverse()

#to copy the list
mylist.copy()

#set items in the list 
mylist.__setitem__(1,'b')

or we can use the following syntax
mylist[1] = 'b'

#to delete an item from the list
del mylist[1]

#to delete the first item from the list
mylist.pop(0)

#to delete the last item from the list
mylist.pop()


# tuples are immutable - once created, they cannot be changed
tuple_data = ("1.Raw Data.txt", "2.Reports.txt", "3.Presentations.txt")
print(type(tuple_data))
# tuples are immutable - once created, they cannot be changed

print(tuple_data[1])


#typecasting is the process of converting one data type to another
a = "10"
a = int(a)
print(a)
print(type(a))

#typecasting to string
b = 10
b = str(b)
print(b)
print(type(b))
