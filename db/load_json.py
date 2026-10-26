import json
from pathlib import Path

# Locate the data folder beside this module.
DATA_DIR = Path(__file__).resolve().parent / "data"


def load_json(json_file):
    # Build the path to the requested JSON file.
    path = DATA_DIR / json_file

    # Read the file and convert its JSON into Python objects.
    with open(path, encoding="utf-8") as file:
        data = json.load(file)

    return data


def convert_tuple(data):
    # Convert each record's values into a tuple in dictionary key order.
    # This order must match the columns listed in the INSERT statement.
    tuple_list = []
    for dict_data in data:
        tuple_list.append(tuple(dict_data.values()))

    return tuple_list