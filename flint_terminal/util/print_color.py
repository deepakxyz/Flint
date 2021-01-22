import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

# color print func


def print_c(type, msg):
    '''
    @pram type: str, level of the message
    @pram msg: str, message to be printed on the terminal
    '''

    # Color globals
    ERROR = Fore.RED
    INFO = Fore.YELLOW
    MSG = Fore.CYAN
    TERM = Back.BLUE

    if type == "ERROR":
        print(f"{ERROR} + {msg}")

    elif type == "INFO":
        print(f"{INFO}{msg}")

    elif type == "MSG":
        print(f"{MSG}{msg}")

    elif type == "TERM":
        return (f"{TERM}{msg}")

    else:
        print(f"{msg}")
