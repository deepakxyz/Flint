import json


# Read json
def read_json(json_file_path):
    with open(json_file_path, 'r') as rf:
        data = rf.read()
        data_json = json.loads(data)
        return data_json


# Write json
def write_json(json_file_path, data):
    with open(json_file_path, 'w') as wf:
        json.dump(data, wf, indent=4)
