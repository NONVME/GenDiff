import json
from typing import TextIO

import yaml


def parse(data: TextIO, ext: str) -> dict:
    """Parse data from file to dict."""
    yaml_formats = ('.yaml', '.yml')
    if ext.lower() in yaml_formats:
        return yaml.safe_load(data)
    return json.load(data)
