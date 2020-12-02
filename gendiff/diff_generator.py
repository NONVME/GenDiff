"""Module for create diff and formatting."""

from gendiff.diff_engine import make_diff
from gendiff.file_reader import get_file_data
from gendiff.formatters.stylish import render


def generate_diff(file1: str, file2: str, style: str) -> str:
    """Generate diff between first and second dicts."""
    data1 = get_file_data(file1)
    data2 = get_file_data(file2)
    diff = make_diff(data1, data2)
    return render(diff, style)
