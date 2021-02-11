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

# create directories


def create_directory(path):
    directories = ['cfx', 'fx', 'lookDev', 'model',
                   'renders', 'rig', 'rnd', 'temp']
    # cfx : character fx (ziva)
    # fx : fx - not sure
    # lookDev : lookDev file (katana or maya file)
    # model : model (zfile)
    # renders : lookDev and test renders
    # rig : rig of the model
    # rnd : research and development
    # temp : temp caches and test export file( will be cleaned)

    # create cat directories
    for dir in directories:
        os.mkdir(path + '\\' + dir)

# Flint create-asset


def create_asset(project, cat, name, assembly, description):
    # asset directory path
    project_path = os.path.join(ROOT_DIR, project)
    cat_path = os.path.join("assets", cat)
    asset_path = os.path.join(project_path, cat_path, name)

    # append data into assets.json
    create_asset_db(project_path, cat, name, assembly, description)

    # create asset directory
    os.mkdir(asset_path)

    # individual asset details that goes inside the asset folder
    asset_details = {
        "name": name,
        "assembly": assembly
    }
    # check if it has assembly

    if assembly == "true" or assembly == "True":
        # create asset subdirectory
        directories = ['assembly']

        # create asset json file
        with open(asset_path + "\\" + name + ".json", "w+") as wf:
            json.dump(asset_details, wf, indent=4)
        for dir in directories:
            os.mkdir(asset_path + '/' + dir)
    # if not assembly
    else:

        with open(asset_path + "\\" + name + ".json", "w+") as wf:
            json.dump(asset_details, wf, indent=4)

        create_directory(asset_path)
# create assembly new asset directory


def create_assembly_subasset_dir(project, cat, asset_name, sub_asset_name):
    project_path = os.path.join(ROOT_DIR, project)
    cat_path = os.path.join("assets", cat)
    asset_path = os.path.join(project_path, cat_path, asset_name)

    # create sub asset directory
    sub_asset_path = os.path.json(asset_path, sub_asset_name)
    os.mkdir(sub_asset_path)
