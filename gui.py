import functions
import PySimpleGUI as sg

#Add name to the window
label = sg.Text("Type in a To-Do")

#Adds a input textboox, where users can type in
input_box = sg.InputText(tooltip = "Enter a to-do", key='todo')

#Adds button with "add" on it
add_button = sg.Button("Add")

window = sg.Window("My To-Do App",
                   layout =[[label,input_box, add_button]],
                  font=('Helvetica', 10))

while True:
    event, values = window.read()
    print(event, values)
    match event:
        case 'Add':
            to_do = functions.get_todos()
            new_todo = values['todo'] + '\n'
            to_do.append(new_todo)
            functions.write_todos(to_do)

        case sg.WINDOW_CLOSED:
            break


window.close()

