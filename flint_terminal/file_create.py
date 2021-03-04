import os
from db.db import ROOT_DIR
from utils import print_c, write_json, read_json

# get asset details
def get_asset_details(project,cat,asset_name):


# create Model file
def create_model_file(project_id, cat, asset_name):
    empty_file = r'Z:\Piper\workbench\copyandrenamefile\empty_ma.mb'
    new_file = os.path.join(ROOT_DIR,project_id,cat,asset_name)
    new_file = os.path.join(new_file , 'll_ch_lou_mod_v001.mb')
    print(new_file)


create_model_file("little_lines","char","lou")