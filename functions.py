FILEPATH = 'todos.txt'
def get_todos(filepath=FILEPATH):
    """Read the text file and return list of
    to-do items """

    with open(filepath, 'r') as file_local:
        todo_local = file_local.readlines()
    return todo_local

def write_todos( todo_arg, filepath=FILEPATH):
    """Write to-do item list into text file"""
    with open(filepath, 'w') as file:
        file.writelines(todo_arg)
