"""Module containing the logic for the gendiff entry-points."""
from gendiff.diff_engine import make_diff
from gendiff.diff_generator import generate_diff
from gendiff.file_reader import get_file_data

__all__ = ['generate_diff', 'make_diff', 'get_file_data']
