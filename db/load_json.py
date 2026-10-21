import json
from pathlib import Path


def load_json():
    # TODO: Make load_json work with any JSON file.

    # Locate users.json relative to this Python file.
    path = Path(__file__).resolve().parent / "data" / "users.json"

    # Read and convert the JSON into Python objects.
    with open(path, encoding="utf-8") as file:
        data = json.load(file)

    return data


def convert_tuple(data):
    # Convert each dictionary's values into a tuple.
    tuple_list = []
    for dict_data in data:
        tuple_list.append(tuple(dict_data.values()))

    return tuple_list