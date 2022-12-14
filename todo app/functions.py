def get_todo():
    with open('todo.txt', 'r') as f:
        todos = f.readlines()
    return todos


def write_todo(todos):
    with open('todo.txt', 'w') as f:
        f.writelines(todos)
