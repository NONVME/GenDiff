"""Module containing the logic for the gendiff entry-points."""
from gendiff.engine import make_diff
from gendiff.file import get_data
from gendiff.generator import generate_diff

__all__ = ['generate_diff', 'make_diff', 'get_data']
