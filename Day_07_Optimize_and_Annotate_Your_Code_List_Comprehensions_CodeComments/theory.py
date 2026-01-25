#list comprehensoin - generation list on fly in a single line
todos = [1,2,3,4]
new_todos = [ i+5 for i in todos]

print(new_todos)

import code
from pydoc import describe


fruits = ["mango\n", "apple\n", "pear\n", "kiwi\n"]
print("old list: ", fruits)

new_fruits = [ item.strip('\n') for item in fruits]
print("new list: ", new_fruits)


using comments to describe your code, we do it using #
# my name is aamir

multiline comment
'''
this is me
my name is aamir
i like to train
'''

