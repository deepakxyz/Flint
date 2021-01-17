import os
from db.db import ROOT_DIR
from utils import read_json

# get all the projects form the root directory


def get_projects():
    projects = os.listdir(ROOT_DIR)
    return projects


# get projects form json file
def get_projects_json(json_file_path):
    data = read_json(json_file_path)
    return data
