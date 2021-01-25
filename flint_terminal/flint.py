import os
from os.path import split
from prettytable import PrettyTable

# Utils function
from utils import print_c

# flint commands
from flint_create import create_project, create_asset
from flint_get import get_projects, get_projects_json

# todos
from todo.todo import get_todos, add_todo, mark_complete, del_todo

# Global Database
from db.db import ROOT_DIR

# terminal input globals
TERMINAL_LOCATION = ">"
PROJECT_LOC = ""
ASSET_TYPE = ""
ASSET_NAME = ""
# about the terminal
print_c("MSG", 'Flint Terminal 1.0.0.')
print_c("MSG", 'Type "help" to see all the commands')

while True:
    terminal_input = ""
    input_cmd = input(f"{PROJECT_LOC}:{TERMINAL_LOCATION}")

    help_note = '''
        FLINT COMMANDS
        create-project                  Create a project.
        cd or project "Project Name"    Move into the project.
        get-p or get-projects           Get all the projects in the root directory.
        root                            Move to the root directory.
        open                            Open the file explorer of the current working directory.

        FLINT ASSET COMMAND
        create-asset                    Create a new asset.

        TODO COMMANDS
        todos                           List all the TODOS.
        todo.add                        Add a new TODO.
        todo.del                        Delete a TODO by index.
        todo.status                     Set TODO status as True or False.


        TERMINAL COMMANDS
        help                            See the help documentation and existing commands.
        exit                            Exit out of the Flint-terminal.
        clear                           Clear the ternimal history.

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

    # change directory
    elif input_cmd.startswith("cd ") or input_cmd.startswith("project "):
        input_data = input_cmd.split(' ')
        if len(PROJECT_LOC) == 0:
            if input_data[1] in get_projects():
                PROJECT_LOC = input_data[1]
            else:
                print_c('ERROR', f"Project '{input_data[1]}' does not exists.")
        else:
            print('Move into asset.')

    # open project explorer
    elif input_cmd.startswith('open'):
        input_data = input_cmd.split(' ')
        if len(input_data) == 2:
            #  open the project directory
            if input_data[1] in get_projects():
                path = os.path.join(ROOT_DIR, input_data[1])
                os.system(f'explorer.exe {path}')

            else:
                print_c('ERROR', f"Project '{input_data[1]}' does not exists.")
        else:
            if PROJECT_LOC in get_projects():
                path = os.path.join(ROOT_DIR, PROJECT_LOC)
                os.system(f'explorer.exe {path}')

            elif PROJECT_LOC == "":
                os.system(f'explorer.exe {ROOT_DIR}')

            else:
                print_c("ERROR", "Project doesn't exists.")

    # Get commands
    # Get all existing projects
    elif input_cmd == "list-p" or input_cmd == "get-p":
        projects = get_projects()
        table = PrettyTable(['Project', 'Description', 'Created on', 'ID'])
        path = os.path.join(ROOT_DIR, 'projects.json')
        data = get_projects_json(path)
        for name in data['projects']:
            table.add_row([name['name'], name['description'],
                           name['created-on'], name['id']])
        print_c("INFO", f"{table}")

    # Working with asset directory and asset

    # create asset
    elif input_cmd == "create-asset":

        asset_type = ['char', 'prop', 'envi', 'matte']
        # check if the currect working directory is a project
        if PROJECT_LOC in get_projects():
            print_c("INFO", "Asset type must be form the following list.")
            print_c("INFO", f"{asset_type}")

            # asset type input from the list
            asset_type_input = input("Asset Type: ")
            if asset_type_input in asset_type:
                print_c("MSG", "    Valid asset type.")

                # asset name input
                asset_name_input = input('Asset Name: ')

                # get assembly value
                print_c("MSG", "type 'true' or 'false' is the assets has assembly.")
                assemble_value = input('Assemble Directory: ')

                if assemble_value == "true" or assemble_value == "false":
                    # create asset directory
                    asset = create_asset(
                        PROJECT_LOC, asset_type_input, asset_name_input, assemble_value)
                    print_c(
                        "MSG", f"Asset '{asset_name_input}' successfully created.")
                else:
                    print_c("ERROR", f'{assemble_value} is invalid.')

            else:
                print_c(
                    "ERROR", f"'{asset_type_input} is not a valid asset type.")

        else:
            print_c(
                "ERROR", "You have to be at the project level to create an asset.")

    # TODOS
    # get all todos
    elif input_cmd == "todos":
        id = 1
        table = PrettyTable(['Id', 'Todos', 'Completed'])
        todos = get_todos()
        for todo in todos['todos']:
            table.add_row([id, todo['todo'], todo['completed']])
            id += 1

        print_c("INFO", f"{table}")

    # add a todo
    elif input_cmd == "todo.add":
        input_data = input("Add a Todo: ")
        add_todo(input_data)
        print_c("INFO", f"Todo added successfully.")

    # delete the todo by index
    elif input_cmd == "todo.del":
        input_data = input("Index of the TODO: ")
        # check if the todo index is out of range
        todos = get_todos()
        if int(input_data) > len(todos['todos']):
            print_c("ERROR", "TODO index out of range.")

        else:
            del_todo(int(input_data))
            print_c("INFO", "Todo deleted successfully.")

    # mark completed
    elif input_cmd == "todo.status":
        input_index = input("Todo Index: ")
        # check if the todo index is out of range
        todos = get_todos()
        if int(input_index) > len(todos['todos']):
            print_c("ERROR", "TODO index out of range.")

        else:
            input_status = input("Todo Status: ")
            if input_status == "True" or input_status == "False":
                mark_complete(input_index, bool(input_status))
                print_c("MSG", "Status marked.")
            else:
                print_c("ERROR", "COMMAND: True or False")

    else:
        print_c(
            "ERROR", f"The command '{input_cmd}' does not exist yet. Use 'help' to find all the commands")
        print('')
