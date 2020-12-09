"""Module containing the logic for the gendiff entry-points."""
from gendiff.engine import make_diff
from gendiff.generator import generate_diff, get_data

__all__ = ['generate_diff', 'make_diff', 'get_data']
