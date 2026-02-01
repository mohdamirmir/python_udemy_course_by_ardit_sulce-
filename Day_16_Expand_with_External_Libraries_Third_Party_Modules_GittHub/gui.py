#!/opt/homebrew/bin/python3.10

from pathlib import Path
import os
import FreeSimpleGUI as sg


os.chdir(Path(__file__).parent)
Path("data").mkdir(exist_ok=True)
Path("data/todos.txt").touch(exist_ok=True)

sg.theme("LightBlue")

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter TO-DO")
add_button = sg.Button("Add")


window = sg.Window( "My TODO-APP",layout=[[label], [input_box,add_button]])

window.read()
print("Hello")
window.close()
