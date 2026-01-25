#reading from and writing into the files
file = open("todos.txt", "r")
# use readlines - this returns a list
todos = file.readlines()
#close the file
file.close()

#difference between readlines and read 
#readlines is used to read the list however read does it for string

#writing into a file
file = open("todos.txt", "w")
file.writelines(todos)
file.close()

# Use file.readlines() when you want to get a list of all lines in the file 
# (for example, for processing each line separately).

# Use file.read() when you want to get the entire contents of the file as a 
# single string (for example, if you want to process or display all the text at once).

# Use file.write() when you want to write a single string (which could have multiple lines if it contains newline characters) to a file.
# Example:
single_line = "This is a single line to write to the file.\n"
file = open("single_line_example.txt", "w")
file.write(single_line)
file.close()

# Use file.writelines() when you have a list (or iterable) of strings and want to write each string to the file.
# Note: writelines does not add newline characters automatically, so include '\n' at the end of each item if you want lines.
lines = ["First line.\n", "Second line.\n", "Third line.\n"]
file = open("multiple_lines_example.txt", "w")
file.writelines(lines)
file.close()


# You can write a multi-line string in Python using double quotes and a backslash (\) to escape line breaks:
multi_line_string = "This is the first line.\
This is the second line.\
This is the third line."
print(multi_line_string)



