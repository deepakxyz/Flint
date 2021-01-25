# copy to clipboard
from subprocess import check_call
import json


def copy2clip(text):
    cmd = 'echo ' + text.strip() + '|clip'
    return check_call(cmd, shell=True)


assets = {
    "assets":
        {
            "char": [],
            "envi": [],
            "matte": [],
            "prop": []
        }

}

with open("temp.json", 'r') as rf:
    data = rf.read()
    data_json = json.loads(data)
    print(data_json)
    print((data_json['assets']['char']))
