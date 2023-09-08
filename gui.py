import functions
import PySimpleGUI as sg
import time

sg.theme('LightGreen2')

clock_label = sg.Text("", key='clock')

#Add name to the window
label = sg.Text("Type in a To-Do")

#Adds a input textboox, where users can type in
input_box = sg.InputText(tooltip = "Enter a to-do", key='todo')

#Adds button with "add" on it
add_button = sg.Button("Add", size=10)

#Get the list of to_dos from functions.py
list_box = sg.Listbox(values=functions.get_todos(), key="todos_items",
                      enable_events=True, size = [45,10])

edit_button = sg.Button("Edit")

complete_button = sg.Button("Complete")

exit_button = sg.Button("Exit")

window = sg.Window("My To-Do App",
                   layout =[[clock_label],
                            [label],
                            [input_box, add_button],
                            [list_box,edit_button, complete_button],
                            [exit_button]],
                  font=('Helvetica', 10))

while True:
    #while loop is being executed evert 10 millisec
    event, values = window.read(timeout=10)
    window['clock'].update(value= time.strftime("%b %d, %Y %H:%M:%S"))
    #print(event, values)
    match event:
        case 'Add':
            todos = functions.get_todos()
            new_todo = values['todo'] + '\n'
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos_items'].update(values = todos)


        case 'Edit':
            try:
                todo_edit = values['todos_items'][0]
                new_to_do = values['todo'] + '\n'
                todos = functions.get_todos()
                index = todos.index(todo_edit)
                todos[index] = new_to_do
                functions.write_todos(todos)

                #updates the list in real-time
                window['todos_items'].update(values = todos)
            except IndexError:
                #pop-up message when they click edit without selecting an item
                sg.popup("Please select an item first.", font=('Helvetica', 10))

        case "todos_items":
            window['todo'].update(value = values['todos_items'][0])

        case 'Complete':
            try:
                todo_complete = values['todos_items'][0]
                todos = functions.get_todos()
                todos.remove(todo_complete)
                functions.write_todos(todos)
                window['todos_items'].update(values = todos)
                window['todo'].update(value='')
            except IndexError:
                #pop-up message when they click complete without selecting an item
                sg.popup("Please select an item first.", font=('Helvetica', 10))


        case "Exit":
            break


        case sg.WINDOW_CLOSED:
            break


window.close()

