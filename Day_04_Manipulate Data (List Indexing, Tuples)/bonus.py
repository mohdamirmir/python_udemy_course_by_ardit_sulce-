filenames = ["1.Raw Data.txt", "2.Reports.txt", "3.Presentations.txt"]

for filename in filenames:
    filename = filename.replace('.','-',1)
    print(filename)

# creating tuples
tuple_data = ("1.Raw Data.txt", "2.Reports.txt", "3.Presentations.txt")
print(type(tuple_data))
# tuples are immutable - once created, they cannot be changed

print(tuple_data[1])

