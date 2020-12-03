"""Testing mod."""
import json

import pytest
from gendiff.diff_generator import generate_diff
from gendiff.formatters.format import JSON, PLAIN, PRETTY

FILE1 = 'tests/fixtures/file1'
FILE2 = 'tests/fixtures/file2'


@pytest.mark.parametrize('ext', ['.json', '.yaml'])
def test_pretty(get_valid_pretty, ext):
    file1 = f'{FILE1}{ext}'
    file2 = f'{FILE2}{ext}'
    assert generate_diff(file1, file2, PRETTY) == get_valid_pretty


@pytest.mark.parametrize('ext', ['.json', '.yaml'])
def test_plain(get_valid_plain, ext):
    file1 = f'{FILE1}{ext}'
    file2 = f'{FILE2}{ext}'
    assert generate_diff(file1, file2, PLAIN) == get_valid_plain


@pytest.mark.parametrize('ext', ['.json', '.yaml'])
def test_json(get_valid_json, ext):
    file1 = f'{FILE1}{ext}'
    file2 = f'{FILE2}{ext}'
    output = generate_diff(file1, file2, JSON)
    assert json.loads(output) == json.loads(get_valid_json)


@pytest.fixture
def get_valid_pretty():
    with open('tests/fixtures/correct_pretty') as file:
        yield file.read()


@pytest.fixture
def get_valid_plain():
    with open('tests/fixtures/correct_plain') as file:
        yield file.read()


@pytest.fixture
def get_valid_json():
    with open('tests/fixtures/correct_json') as file:
        yield file.read()
