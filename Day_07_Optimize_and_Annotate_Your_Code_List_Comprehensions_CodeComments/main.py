from pathlib import Path
import os

os.chdir(Path(__file__).parent)

while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    match user_action:
        case 'add':
            # print(os.getcwd())
            todo = input("enter a todo: ") + "\n"

            file = open("data/todos.txt", "r")
            todos = file.readlines()
            file.close()

            todos.append(todo)


            file = open("data/todos.txt", "w")
            todos = file.writelines()
            file.close()

        case 'show':

            file = open("data/todos.txt", "r")
            todos = file.readlines()
            file.close()

            # new_todos = [item.strip('\n') for item in todos]
            # print(new_todos)

            for index,item in enumerate(todos):
                item = item.strip('\n')
                row = f"{index+1}-{item}"
                print(row)

        case 'edit':
            number = int(input("Number of the todo to edit: ")) 
            number = number - 1
            new_todo = input("Enter new todo: ")
            todos[number] = new_todo
        
        case 'complete':
            number =int(input("Number of the todo to complete: "))
            number = number - 1
            todos.pop(number)

        case 'exit':
            break

        case _:
            print("Hey! you printed an unknown command")

print("Bye!")
