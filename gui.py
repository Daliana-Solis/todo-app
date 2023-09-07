import functions
import PySimpleGUI as sg

#Add name to the window
label = sg.Text("Type in a To-Do")

#Adds a input textboox, where users can type in
input_box = sg.InputText(tooltip = "Enter a to-do")

#Adds button with "add" on it
add_button = sg.Button("Add")

window = sg.Window("My To-Do App", layout =[[label], [input_box, add_button]])
window.read()
window.close()

