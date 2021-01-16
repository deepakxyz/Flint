import json


# Read json
def read_json(json_file_path):
    with open(json_file_path, 'r') as rf:
        data = rf.read()
        data_json = json.loads(data)
        return data_json


def write_json(json_file_path, data):
    with open(json_file_path, 'w') as f:
        json.dump(data, f, indent=4)
