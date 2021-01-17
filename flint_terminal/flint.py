import os
from os.path import split
from prettytable import PrettyTable

# Utils function
from utils import print_c

# flint commands
from flint_create import create_project
from flint_get import get_projects, get_projects_json

# todos
from todo.todo import get_todos, add_todo

# Global Database
from db.db import ROOT_DIR

# terminal input globals
TERMINAL_LOCATION = "$ >"
PROJECT_LOC = ""
# about the terminal
print_c("MSG", 'Flint Terminal 1.0.0.')
print_c("MSG", 'Type "help" to see all the commands')

while True:
    terminal_input = ""
    input_cmd = input(f"{PROJECT_LOC} {TERMINAL_LOCATION}")

    help_note = '''
        create-project - Create a project.
        project "Project Name" - Move into the project.
        root - Move to the root directory.

        Terminal Command
        help - See the help documentationa and existing command.
        exit - Exit out of the Flint-terminal.
        clear - Clear the ternimal history.

    '''

    # help
    if input_cmd == "help" or input_cmd == "-h":
        print_c("INFO", help_note)

    # exit
    elif input_cmd == "exit":
        break

    # clear terminal history
    elif input_cmd == "clear":
        os.system('clear')
        print_c("MSG", 'Flint Terminal 1.0.0.')
        print_c("MSG", 'Type "help" to see all the commands')

    # go to the root directory
    elif input_cmd == "root":
        PROJECT_LOC = ''

    # create a project
    elif input_cmd == "create-project":
        if PROJECT_LOC:
            print_c(
                'ERROR', f"New project cannot be created when your are inside the project. Type 'root' to move to the root directory")
        else:
            name = input("Project Name:")
            # check if the project name has spaces
            split_name = name.split(' ')
            if len(split_name) > 1:
                print_c(
                    'ERROR', "Cannot use spaces in your project name, insted use '_'")
                name = input("Project Name:")
            description = input("Project Description:")
            create_project(name, description)
            print_c('INFO', f"Project '{name}' successfully created.")
            print('')

    # change directory into project
    elif input_cmd.startswith("cd ") or input_cmd.startswith("project "):
        input_data = input_cmd.split(' ')
        if input_data[1] in get_projects():
            PROJECT_LOC = input_data[1]
        else:
            print_c('ERROR', f"Project '{input_data[1]}' does not exists.")

    # open project explorer
    elif input_cmd.startswith('open'):
        input_data = input_cmd.split(' ')
        if len(input_data) == 2:
            if input_data[1] in get_projects():
                path = os.path.join(ROOT_DIR, input_data[1])
                os.system(f'explorer.exe {path}')
            else:
                print_c('ERROR', f"Project '{input_data[1]}' does not exists.")
        else:
            if PROJECT_LOC in get_projects():
                path = os.path.join(ROOT_DIR, PROJECT_LOC)
                os.system(f'explorer.exe {path}')

    # Get commands
    # Get all existing projects
    elif input_cmd == "get-projects" or input_cmd == "get-p":
        projects = get_projects()
        table = PrettyTable(['Project', 'Description', 'Created on', 'ID'])
        path = os.path.join(ROOT_DIR, 'projects.json')
        data = get_projects_json(path)
        for name in data['projects']:
            table.add_row([name['name'], name['description'],
                           name['created-on'], name['id']])
        print_c("INFO", f"{table}")

    # TODOS
    # get all todos
    elif input_cmd == "todos":
        id = 1
        table = PrettyTable(['Id', 'Todos'])
        todos = get_todos()
        for todo in todos['todos']:
            table.add_row([id, todo['todo']])
            id += 1

        print_c("INFO", f"{table}")

    # add new todo
    elif input_cmd == "todo.add":
        new_todo = input('Add a Todo:')
        add_todo(new_todo)

    else:
        print_c(
            "ERROR", f"The command '{input_cmd}' does not exist yet. Use 'help' to find all the commands")
        print('')
