#default arguments
# non default arguments have to be before default arguments, however we can also change the 
#value of default arguments
def greeting(name, message="Hello, how are you", ):
    """ Returns a greeting message """
    print(f"{message} {name}")

greeting("aamir")

greeting("aamir", "Welcome to dubai")

# docstrings for help
# we can specify these strings at the start of the function in these triple quotes """ """,
# they are also referred to as multi-line strings


print(help(greeting))

python 3.11.2
      major.minor.patch  

major versions are not backward compatible

