import urllib.request
import json


def get_remote_data(url: str, default_file: str):
    """
    Get remote JSON data
    If there is not data from remote service return the default data for specified file

    Parameters
        remote_path : str -> url where information is going to be accessed
        default_file : str -> Default file into the project to get in case [url] return an error
    """
    try:
        # Get the messages from a remote JSON file
        with urllib.request.urlopen(url) as remote_data:
            data = json.loads(remote_data.read().decode())
    except:
        # If there is an error, use the default messages file
        with open(default_file, 'r') as file:
            data = json.load(file)
    return data
