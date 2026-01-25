from email import message
from pathlib import Path
import os

os.chdir(Path(__file__).parent)
Path("data").mkdir(exist_ok=True)
Path("data/todos.txt").touch(exist_ok=True)

while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    match user_action:
        case 'add':
            # print(os.getcwd())
            todo = input("enter a todo: ") + "\n"

            with open("data/todos.txt", "r") as file:
                todos = file.readlines()

            todos.append(todo)

            with open("data/todos.txt", "w") as file:
                file.writelines(todos)
        
        case 'show':
            with open("data/todos.txt", "r") as file:
                todos = file.readlines()

            for index,item in enumerate(todos):
                item = item.strip('\n')
                row = f"{index+1}-{item}"
                print(row)

        case 'edit':
            number = int(input("Number of the todo to edit: ")) 
            number = number - 1

            with open("data/todos.txt", "r") as file:
                todos = file.readlines()

            new_todo = input("Enter new todo: ")
            todos[number] = new_todo + "\n"

            with open("data/todos.txt", "w") as file:
                file.writelines(todos)


        case 'complete':
            number =int(input("Number of the todo to complete: "))
            index = number - 1

            with open("data/todos.txt", "r") as file:
                todos = file.readlines()
                
            todo_to_remove = todos[index].strip('\n')

            todos.pop(index)

            with open("data/todos.txt", "w") as file:
                file.writelines(todos)
            
            message = f"Todo {todo_to_remove} was removed from the list"
            print(message)

        case 'exit':
            break

        case _:
            print("Hey! you printed an unknown command")

print("Bye!")
