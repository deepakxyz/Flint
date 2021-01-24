import json
import os
from time import gmtime, strftime

# database template
from .db import ROOT_DIR, PROJECTS_JSON, PROJECT_BASE_ID
from .db_json import read_json, write_json


def create_project_db(name, description):

    # check if the projects json file exists
    projects_json_path = os.path.join(ROOT_DIR, PROJECTS_JSON)

    # create-project
    # get data from the json
    data = read_json(projects_json_path)
    # data = data['projects']

    # created date
    created_on = strftime("%d %b %Y", gmtime())

    # create project Id
    project_id = PROJECT_BASE_ID + len(data['projects'])
    # new projct detail and append into a dic
    new_project_data = {"name": name, "description": description,
                        "created-on": created_on, "id": project_id}
    data['projects'].append(new_project_data)

    # dump data into json file
    write_json(projects_json_path, data)

    return new_project_data


# Create asset
def create_asset_db(name, description):
    pass
