import os
from db.create_db import create_project_db
from db.db import ROOT_DIR
from utils import print_c, write_json


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
