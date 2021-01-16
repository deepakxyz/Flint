import json


# Read json
def read_json(json_file_path):
    with open(json_file_path, 'r') as rf:
        data = rf.read()
        data_json = json.loads(data)
        return data_json


def create_project_json(json_file_path):
    # read and get json file data
    data_json = read_json(json_file_path)
