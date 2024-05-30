#!/usr/bin/python3
import json


def serialize_and_save_to_file(data, filename):
    """Serialize the py dict 'data' to a JSON file specified by 'filename'.

    Parameters:
    data (dict): The dictionary to serialize.
    filename (str): Name of the serialized data save."""
    with open(filename, 'w') as file:
        json.dump(data, file)


def load_and_deserialize(filename):
    """
    Load and deserialize JSON data from the file to a dictionary.

    Parameters:
    filename (str): Name of file to load the JSON data from.

    Returns:
    dict: The deserialized Python dictionary.
    """
    with open(filename, 'r') as file:
        data = json.load(file)
    return data
