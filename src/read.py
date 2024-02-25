import json

def read(file_name):
    with open(f"data/{file_name}.json", "r") as file:
        json_object = json.load(file)
    return json_object