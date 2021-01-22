# copy to clipboard
from subprocess import check_call


def copy2clip(text):
    cmd = 'echo ' + text.strip() + '|clip'
    return check_call(cmd, shell=True)


text = "Error, This is your fucking error."
copy2clip(text)
