import os

# Utils function
from util.print_color import print_c

# terminal input globals
TERMINAL_LOCATION = "$ >"

# about the terminal
print_c("MSG", 'Flint Terminal 1.0.0.')
print_c("MSG", 'Type "help" to see all the commands')

while True:
    terminal_input = ""
    input_cmd = input(f"{TERMINAL_LOCATION}")

    # help
    if input_cmd == "help" or input_cmd == "-h":
        print_c("INFO", "This is the test")

    # clear terminal history
    elif input_cmd == "clear":
        os.system('clear')

    else:
        print_c(
            "ERROR", f"The command '{input_cmd} does not exist yet. Use 'help' to find all the commands")
