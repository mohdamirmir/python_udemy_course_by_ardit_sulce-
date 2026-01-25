from pathlib import Path
# TODOS_PATH = Path(__file__).parent.parent / "data" / "todos.txt"
# import os

while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    match user_action:
        case 'add':
            # print(os.getcwd())
            todo = input("enter a todo: ") + "\n"

            # file = open(TODOS_PATH, 'r')
            file = open("data/todos.txt", "r")
            todos = file.readlines()
            file.close()

            todos.append(todo)

            # file = open(TODOS_PATH, 'w')
            file = open("data/todos.txt","w")
            file.writelines(todos)
            file.close()
        
        case 'show':
            # file = open(TODOS_PATH,"r")
            file = open("./data/todos.txt","r")
            todos = file.readlines()
            file.close()

            for index,item in enumerate(todos):
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