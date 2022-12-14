import PySimpleGUI as sg
from functions import get_todo, write_todo


text = sg.Text("Enter todo")
input_box = sg.Input(key='input')
button = sg.Button('Add')
list_box = sg.Listbox(values=get_todo(),enable_events=True, key='show', size=(45, 10))
edit_button = sg.Button('Edit')
complete_button=sg.Button('complete')

window = sg.Window('To-Do App', layout=[[text, input_box, button], [list_box, edit_button , complete_button]])

while True:
    event, value = window.read()


    match event:

        case 'show':
            window['input'].update(value=value['show'][0])

        case 'Add':
            value['input'] = value['input'] + "\n"
            todos = get_todo()
            todos.append(value['input'])
            write_todo(todos)

            window['show'].update(values=todos)


        case 'Edit':
            old_to_do = value['show'][0]
            new_to_do = value['input']
            new_to_do=new_to_do+"\n"
            todos = get_todo()
            index = todos.index(old_to_do)
            todos[index] = new_to_do
            write_todo(todos)

            window['show'].update(values=todos)

        case 'complete':
            todo=value['show'][0]
            todos=get_todo()
            todos.remove(todo)
            write_todo(todos)

            window['show'].update(values=todos)
            window['input'].update(value='')
        case sg.WIN_CLOSED:
            break

window.close()
