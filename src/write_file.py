import json


def write_file(data, file_name):
    json_object = json.dumps(data, indent=4)
 
    with open(f"data/{file_name}.json", "w") as outfile:
        outfile.write(json_object)

