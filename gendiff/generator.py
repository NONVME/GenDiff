"""Module for create diff and formatting."""
from gendiff import file
from gendiff.engine import make_diff
from gendiff.formatters import format


def generate_diff(file1: str, file2: str, style: str) -> str:
    """Generate diff between first and second dicts."""
    data1 = file.get_data(file1)
    data2 = file.get_data(file2)
    diff = make_diff(data1, data2)
    return format.build(diff, style)
