import time
from functions import get_todo, write_todo

todos = []

while True:
    user_input = input("Type Add,show,edit,complete,exit tasks:")
    user_input = user_input.strip()

    if user_input.startswith('add'):
        todo = user_input[4:]
        todo = todo + "\n"

        todos = get_todo()
        todos.append(todo)

        write_todo(todos)

    elif user_input.startswith('show'):
        with open("todo.txt", 'r') as f:
            todos = f.readlines()
            new_todos = [x.strip("\n") for x in todos]
        for index, x in enumerate(new_todos):
            print(index, " ", x)

    elif user_input.startswith('edit'):
        try:
            number = int(input("Enter number of todo to edit: "))
            todo = todos[number]
            todo = todo.strip("\n")
            print("Present todo: ", todo)
            new_todo = input("Enter new todo: ")
            new_todo = new_todo + "\n"
            todos[number] = new_todo

            write_todo(todos)

        except ValueError:
            print("Enter number of todo task")
            continue


    elif user_input.startswith('complete'):
        number = int(input("Enter number of todo to complete: "))
        print("Todo: ", todos[number])
        todos.remove(todos[number])
        write_todo(todos)

    elif user_input.startswith('exit'):
        break

    else:
        print("Invalid")

print("End")
