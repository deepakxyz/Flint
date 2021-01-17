from colorama import Fore, Back, Style
import colorama
import json


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


# color print func
colorama.init(autoreset=True)


def print_c(type, msg):
    '''
    @pram type: str, level of the message
    @pram msg: str, message to be printed on the terminal
    '''

    # Color globals
    ERROR = Fore.RED
    INFO = Fore.YELLOW
    MSG = Fore.CYAN

    if type == "ERROR":
        print(f"{ERROR} + {msg}")

    elif type == "INFO":
        print(f"{INFO}{msg}")

    elif type == "MSG":
        print(f"{MSG}{msg}")

    else:
        print(f"{msg}")
