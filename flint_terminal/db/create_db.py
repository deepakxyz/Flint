import json
import os


# database template
from db import ROOT_DIR, PROJECTS_JSON
from ..util.rw_json import new


def create_project_db(name):

    # check if the projects json file exists
    projects_json_path = os.path.join(ROOT_DIR, PROJECTS_JSON)
    if os.path.isfile(projects_json_path):
        # Read the json file
        data = read_json(projects_json_path)
        print(data)
    else:
        pass


new()
