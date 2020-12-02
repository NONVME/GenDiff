import json
import os

import yaml


def get_file_data(path: str) -> dict:
    """Parse data from file to dict."""
    yaml_formats = ('.yaml', '.yml')
    fullpath = os.path.abspath(path)
    _, ext = os.path.splitext(path)
    with open(fullpath, 'r', encoding='utf-8') as file:
        if ext.lower() in yaml_formats:
            return yaml.safe_load(file)
        return json.load(file)
