import json
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


def get_assets(project):
    assets_path = os.path.join(ROOT_DIR, project)
    assets_json_file = os.path.join(assets_path, "assets", "assets.json")
    data = read_json(assets_json_file)
    return data


def get_asset_details(project, type, asset):
    project_path = os.path.join(ROOT_DIR, project)
    asset_path = os.path.join(project_path, "assets", type, asset)
    json_file_name = asset + ".json"
    asset_json_file = os.path.join(asset_path, json_file_name)
    data = read_json(asset_json_file)
    return data
