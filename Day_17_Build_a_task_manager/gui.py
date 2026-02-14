#!/opt/homebrew/bin/python3.10

from pathlib import Path
from re import S
from modules import functions
import os
import FreeSimpleGUI as sg
import time


os.chdir(Path(__file__).parent)
Path("data").mkdir(exist_ok=True)
Path("data/todos.txt").touch(exist_ok=True)

sg.theme("DarkGreen4")

clock = sg.Text('', key="clock")
label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter TO-DO", key="todo")
add_button = sg.Button("Add")
list_box = sg.Listbox(values=functions.get_todos(), key="todos",
                      enable_events=True, size=(45, 10))
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")

layout = [[clock],
          [label], 
          [input_box,add_button], 
          [list_box, edit_button, complete_button],
          [exit_button]]

window = sg.Window( "My TODO-APP",
                    layout=layout,
                    font=("Helvetica", 20))



while True:
    event, values = window.read(timeout=200)
    window["clock"].update(value=time.strftime("%b %d, %Y %H:%M:%S"))
    print(1,event)
    print(2,values)
    print(3,values["todos"])
    print(4,values["todo"])
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values["todo"].strip()
            if not new_todo:
                continue
            new_todo = new_todo + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window["todos"].update(values=todos)

        case "Edit":
            try:
                new_todo = values["todo"] + "\n"
                todo_to_edit = values["todos"][0]
                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                functions.write_todos(todos)
                window["todos"].update(values=todos)
        
            except IndexError as e:
                sg.popup("Please select an item first", font=("Helvetica", 20))

        case "Complete":
            try:
                todo_to_complete = values["todos"][0]
                todos = functions.get_todos()
                todos.remove(todo_to_complete)  
                functions.write_todos(todos)  
                window["todos"].update(values=todos)   
                window["todo"].update(value="")
            except IndexError:
                sg.popup("Please select an item first", font=("Helvetica", 20))


        case "todos":
            if values["todos"]:
                window["todo"].update(value=values["todos"][0].strip())
        
        case "Exit":
            break

        case sg.WIN_CLOSED:
            break
            
window.close()
