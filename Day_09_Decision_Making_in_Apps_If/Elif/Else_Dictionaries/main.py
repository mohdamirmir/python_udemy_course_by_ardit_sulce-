from email import message
from pathlib import Path
import os

os.chdir(Path(__file__).parent)
Path("data").mkdir(exist_ok=True)
Path("data/todos.txt").touch(exist_ok=True)

while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    if 'add' in user_action:
        # print(os.getcwd())
        todo = user_action[4:]

        with open("data/todos.txt", "r") as file:
            todos = file.readlines()

        todos.append(todo)

        with open("data/todos.txt", "w") as file:
            file.writelines(todos)
    
    elif 'show' in user_action:
        with open("data/todos.txt", "r") as file:
            todos = file.readlines()

        for index,item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index+1}-{item}"
            print(row)

    elif 'edit' in user_action:
        number = int(user_action[5:])
        number = number - 1

        with open("data/todos.txt", "r") as file:
            todos = file.readlines()

        new_todo = input("Enter new todo: ")
        todos[number] = new_todo + "\n"

        with open("data/todos.txt", "w") as file:
            file.writelines(todos)


    elif 'complete' in user_action:
        number = int(user_action[9:])
        index = number - 1

        todo_to_remove = todos[index].strip('\n')

        with open("data/todos.txt", "r") as file:
            todos = file.readlines()
            
        todos.pop(index)

        with open("data/todos.txt", "w") as file:
            file.writelines(todos)
        
        message = f"Todo {todo_to_remove} was removed from the list"
        print(message)

    elif 'exit' in user_action:
            break
    
    else:
        print("the command is not valid")

print("Bye!")
