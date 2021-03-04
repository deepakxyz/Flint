import os
from time import gmtime, strftime

# database template
from .db import ROOT_DIR, PROJECTS_JSON, PROJECT_BASE_ID, ASSETS_JSON, ASSET_BASE_ID
from .db_json import read_json, write_json


def create_project_db(name, description, id):

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
                        "created-on": created_on, "id": id}
    data['projects'].append(new_project_data)

    # dump data into json file
    write_json(projects_json_path, data)

    return new_project_data


# Create asset
def create_asset_db(projectLoc, assetType, assetName, assembly=True, description="None"):

    # assets.json file path
    assets_json_path = os.path.join(
        projectLoc, "assets", "assets.json")

    # get data from the json
    data = read_json(assets_json_path)

    # created date
    created_on = strftime("%d %b %Y", gmtime())

    # create asset ID
    asset_id = ASSET_BASE_ID + len(data['assets'][assetType])

    # new assets json template
    new_asset_template = {
        "name": assetName,
        "created-on": created_on,
        "id": asset_id,
        "assembly": assembly,
        "status": False,
        "description": description
    }

    data['assets'][assetType].append(new_asset_template)

    # dump the json data
    write_json(assets_json_path, data)
