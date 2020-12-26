import json

import yaml


def parse(data: str, ext: str) -> dict:
    """Parse data from file to dict."""
    yaml_formats = ('.yaml', '.yml')
    if ext.lower() in yaml_formats:
        return yaml.safe_load(data)
    elif ext.lower() == '.json':
        return json.loads(data)
    raise ValueError(f'Unhandled file extension {ext}')
