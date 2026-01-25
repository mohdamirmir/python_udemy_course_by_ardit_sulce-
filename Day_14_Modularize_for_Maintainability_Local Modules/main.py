from pathlib import Path
import os

os.chdir(Path(__file__).parent)
Path("data").mkdir(exist_ok=True)
Path("data/todos.txt").touch(exist_ok=True)
# from functions import get_todos, write_todos

from modules import functions

while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith('add'):
        # print(os.getcwd())
        todo = user_action[4:] + '\n'
        todos = functions.get_todos()
        todos.append(todo)
        functions.write_todos(todos)
    
    elif user_action.startswith('show'):
        todos = functions.get_todos()

        for index,item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1}-{item}"
            print(row)

    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            print(number)
            number = number - 1
            todos = functions.get_todos()
            new_todo = input("Enter new todo: ")
            todos[number] = new_todo + "\n"
            functions.write_todos(todos)

        except ValueError:
            print("Your command is not valid.")
            continue

    elif user_action.startswith('complete'):
        try:

            number = int(user_action[9:])
            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos = functions.get_todos()
            todos.pop(index)
            functions.write_todos(todos)
            message = f"Todo {todo_to_remove} was removed from the list"
            print(message)
        except IndexError:
            print("there is no item with that number")


    elif user_action.startswith('exit'):
            break
    
    else:
        print("the command is not valid")


print("Bye!")
