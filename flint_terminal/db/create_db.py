import json
import os


# database template
from db import ROOT_DIR, PROJECTS_JSON
from db_json import read_json, create_project_json


def create_project_db(name):

    # check if the projects json file exists
    projects_json_path = os.path.join(ROOT_DIR, PROJECTS_JSON)
    if os.path.isfile(projects_json_path):
        # Read the json file
        # data = read_json(projects_json_path)
        # print(data)
        pass
    else:
        pass

    # check if the project already exists
        # load all the project name form the json file
        # check if there is a folder name by project name
        # return, the project already exists

    # else:
        # create-project


create_project_db("project")
