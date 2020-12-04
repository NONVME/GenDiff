"""Testing mod."""
import json

import pytest

from gendiff.diff_generator import generate_diff
from gendiff.formatters.format import JSON, PLAIN, PRETTY

FILE1 = 'tests/fixtures/file1'
FILE2 = 'tests/fixtures/file2'
CORRECT_PRETTY = 'tests/fixtures/correct_pretty'
CORRECT_PLAIN = 'tests/fixtures/correct_plain'
CORRECT_JSON = 'tests/fixtures/correct_json'


@pytest.mark.parametrize('ext', ['.json', '.yaml'])
def test_generate_diff(ext):
    file1 = f'{FILE1}{ext}'
    file2 = f'{FILE2}{ext}'
    output = generate_diff(file1, file2, JSON)
    assert generate_diff(file1, file2, PRETTY) ==read_file(CORRECT_PRETTY)
    assert generate_diff(file1, file2, PLAIN) ==read_file(CORRECT_PLAIN)
    assert json.loads(output) == json.loads(read_file(CORRECT_JSON))


def read_file(file_path):
    with open(file_path) as file:
        return file.read()
