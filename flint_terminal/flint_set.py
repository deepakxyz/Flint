import json
import os
from db.db import ROOT_DIR, FLINT_DIR
from utils import read_json, write_json

DB_JSON = os.path.join(FLINT_DIR, "db","quick.json")

# get level
def get_level_db(level_id):
    data = read_json(DB_JSON)
    level_data = data['level']
    return level_data[level_id]

# set level
def set_level_db(level_id,project_name, asset_type, asset_name):
    data = read_json(DB_JSON)
    data['level'][level_id]['project_name'] = project_name
    data['level'][level_id]['asset_type'] = asset_type
    data['level'][level_id]['asset_name'] = asset_name
    write_json(DB_JSON, data)
