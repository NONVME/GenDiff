import os

from gendiff.parser import parse


def get_data(path: str) -> dict:
    """Read data from file."""
    fullpath = os.path.abspath(path)
    _, ext = os.path.splitext(path)
    with open(fullpath, 'r', encoding='utf-8') as row_data:
        return parse(row_data, ext)
