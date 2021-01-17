import json

TODO_PATH = "Y:\\Flint\\flint_terminal\\todo\\todos.json"

# Read json


def read_json(json_file_path):
    with open(json_file_path, 'r') as rf:
        data = rf.read()
        data_json = json.loads(data)
        return data_json


# Write json
def write_json(json_file_path, data):
    with open(json_file_path, 'w') as wf:
        json.dump(data, wf, indent=4)


def todos():
    todos = read_json('todos.json')
    del todos['todos'][1]
    print(todos)

# get all the todos


def get_todos():
    todos = read_json(TODO_PATH)
    return todos

# add new todo


def add_todo(todo):
    # get the todos
    todos = read_json(TODO_PATH)
    new_todo = {"todo": todo}
    todos['todos'].append(new_todo)
    write_json(TODO_PATH, todos)
