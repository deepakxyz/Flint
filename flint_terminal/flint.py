import os

# Utils function
from util.print_color import print_c

# flint commands
from flint_create import create_project

# terminal input globals
TERMINAL_LOCATION = "$ >"

# about the terminal
print_c("MSG", 'Flint Terminal 1.0.0.')
print_c("MSG", 'Type "help" to see all the commands')

while True:
    terminal_input = ""
    input_cmd = input(f"{TERMINAL_LOCATION}")

    help_note = '''
        create-project - Create a project
    '''

    # help
    if input_cmd == "help" or input_cmd == "-h":
        print_c(help_note)

    # exit
    elif input_cmd == "exit":
        break

    # clear terminal history
    elif input_cmd == "clear":
        os.system('clear')

    # create a project
    elif input_cmd == "create-project":
        name = input("Project Name:")
        description = input("Project Description:")
        create_project(name, description)
        print_c('INFO', f"Project '{name}' successfully created.")
        print('')

    else:
        print_c(
            "ERROR", f"The command '{input_cmd} does not exist yet. Use 'help' to find all the commands")
