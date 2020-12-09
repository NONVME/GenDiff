"""Module for create diff and formatting."""
import os

from gendiff.engine import make_diff
from gendiff.formatters import format
from gendiff.parser import ext_parser


def generate_diff(file1: str, file2: str, style: str) -> str:
    """Generate diff between first and second dicts."""
    data1 = get_data(file1)
    data2 = get_data(file2)
    diff = make_diff(data1, data2)
    return format.build(diff, style)


def get_data(path: str) -> dict:
    """Read data from file."""
    fullpath = os.path.abspath(path)
    _, ext = os.path.splitext(path)
    with open(fullpath, 'r', encoding='utf-8') as row_data:
        return ext_parser(row_data, ext)
