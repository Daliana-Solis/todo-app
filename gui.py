import functions
import PySimpleGUI as sg

#Add name to the window
label = sg.Text("Type in a To-Do")

#Adds a input textboox, where users can type in
input_box = sg.InputText(tooltip = "Enter a to-do", key='todo')

#Adds button with "add" on it
add_button = sg.Button("Add")

#Get the list of to_dos from functions.py
list_box = sg.Listbox(values=functions.get_todos(), key="todos_items",
                      enable_events=True, size = [45,10])

edit_button = sg.Button("Edit")

window = sg.Window("My To-Do App",
                   layout =[[label],
                            [input_box, add_button],
                            [list_box,edit_button]],
                  font=('Helvetica', 10))

while True:
    event, values = window.read()
    print(event, values)
    match event:
        case 'Add':
            todos = functions.get_todos()
            new_todo = values['todo'] + '\n'
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos_items'].update(values = todos)


        case 'Edit':
            todo_edit = values['todos_items'][0]
            new_to_do = values['todo'] + '\n'
            todos = functions.get_todos()
            index = todos.index(todo_edit)
            todos[index] = new_to_do
            functions.write_todos(todos)

            #updates the list in real-time
            window['todos_items'].update(values = todos)

        case "todos_items":
            window['todo'].update(value = values['todos_items'][0])


        case sg.WINDOW_CLOSED:
            break


window.close()

