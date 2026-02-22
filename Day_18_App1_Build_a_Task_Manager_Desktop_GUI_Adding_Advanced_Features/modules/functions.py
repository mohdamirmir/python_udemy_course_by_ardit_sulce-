

def get_todos(filepath="data/todos.txt"):
    '''
    Read a text file and return a list of to-do items
    '''
    with open(filepath, "r") as local_file:
            todos_local = local_file.readlines()
    return todos_local

def write_todos(todos_arg, filepath="data/todos.txt"):
    '''
    Write the to-d0 list items to the text file
    '''    
    with open(filepath, "w") as local_file:
            local_file.writelines(todos_arg)

print(__name__)

