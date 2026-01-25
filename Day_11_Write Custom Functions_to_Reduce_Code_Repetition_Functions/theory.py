from email import message


functions
-----------
#used for reducing the redunduncy

#function definitin
def get_todos():
    with open("file.txt", "r") as file:
        todos = file.readlines()
    return todos


#function call
get_todos()


#scope - variables are available within their scope which means we can access the variable 
# of a function inside that function only

def greet():
    message = "hello"
    new_message = message.capitalize()
    return new_message


output= greet()

#this will work
print(output)

#this will not as here u are using variable out of its scope
print(new_message)

'''
if you dont return anything from the function it will return None, None is a special
value and not a string
'''

'''
python is best suited for web development, data science etc
java is for desktop apps, mobile apps
'''

'''
Another benefit of creating functions is to make your code easier to extend and reuse. 
Being a well-defined block of code a function is easy to copy and paste into other 
programs you are writing.
For example, you might have created a function that converts an image to greyscale in 
the Python photo editing program you have created. You can reuse that function in 
another program where you are processing video to convert the video frames to greyscale.
Likewise, a function can also be used in different parts of the same program. 
In other words, functions will keep your codebase more organized.
'''
