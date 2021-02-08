import os
from db.create_db import create_project_db, create_asset_db
from db.db import ROOT_DIR
from utils import print_c, write_json, read_json
import json


# create-project command
def create_project(name, description):
    path = os.path.join(ROOT_DIR, name)
    # check if the project already exists
    if os.path.isdir(path):
        print_c('MSG', f"Project by the name '{name}' already exists.")

    # else create the project
    else:
        # dump data into main projects json file
        data = create_project_db(name, description)
        # create directory
        os.mkdir(path)
        # create a seprate json file inside the project directory
        current_project_path = os.path.join(path, "details.json")
        write_json(current_project_path, data)

        # create asset category directories
        create_assets_seq_dir(path)


def create_assets_seq_dir(path):
    # directory
    dirs = ['assets', 'sequences']
    for dir in dirs:
        dir_path = os.path.join(path, dir)
        os.mkdir(dir_path)
        if dir == "assets":
            # create asset category
            create_assets_cat(dir_path)
        else:
            pass


# Create asset cat directories.
def create_assets_cat(path):
    # asset category
    asset_cat = ["char", "prop", "envi", "matte"]
    for cat in asset_cat:
        cat_path = os.path.join(path, cat)
        os.mkdir(cat_path)

    # assets.json template
    assets_template = {
        "assets": {
            "char": [],
            "envi": [],
            "matte": [],
            "prop": []
        }
    }

    # create assets.json
    with open(path + "\\assets.json", "w+") as wf:
        json.dump(assets_template, wf, indent=4)


# Flint create-asset
def create_asset(project, cat, name, assembly):
    # asset directory path
    project_path = os.path.join(ROOT_DIR, project)
    cat_path = os.path.join("assets", cat)
    asset_path = os.path.join(project_path, cat_path, name)

    # append data into assets.json
    create_asset_db(project_path, cat, name, assembly)

    # create asset directory
    os.mkdir(asset_path)

    # check if it has assembly
    if assembly:
        # create asset subdirectory
        pass

    # if not assembly
    else:
        pass
