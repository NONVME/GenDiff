"""Testing mod."""
import json

import pytest
from gendiff.formatters.stylish import JSON, PLAIN, PRETTY
from gendiff.generate_diff import generate_diff


JSON_FILE1 = 'tests/fixtures/file1.json'
JSON_FILE2 = 'tests/fixtures/file2.json'
YAML_FILE1 = 'tests/fixtures/file1.yaml'
YAML_FILE2 = 'tests/fixtures/file2.yaml'


def test_pretty(get_correct_pretty):
    check_answer_json = generate_diff(JSON_FILE1, JSON_FILE2, PRETTY)
    check_answer_yaml = generate_diff(YAML_FILE1, YAML_FILE2, PRETTY)
    assert check_answer_json == get_correct_pretty
    assert check_answer_yaml == get_correct_pretty


def test_plain(get_correct_plain):
    check_answer_json = generate_diff(JSON_FILE1, JSON_FILE2, PLAIN)
    check_answer_yaml = generate_diff(YAML_FILE1, YAML_FILE2, PLAIN)
    assert check_answer_json == get_correct_plain
    assert check_answer_yaml == get_correct_plain


def test_json(get_correct_json):
    check_answer_json = generate_diff(JSON_FILE1, JSON_FILE2, JSON)
    check_answer_yaml = generate_diff(YAML_FILE1, YAML_FILE2, JSON)
    assert json.loads(check_answer_json) == json.loads(get_correct_json)
    assert json.loads(check_answer_yaml) == json.loads(get_correct_json)


@pytest.fixture
def get_correct_pretty():
    with open('tests/fixtures/correct_pretty') as file:
        yield file.read()


@pytest.fixture
def get_correct_plain():
    with open('tests/fixtures/correct_plain') as file:
        yield file.read()


@pytest.fixture
def get_correct_json():
    with open('tests/fixtures/correct_json') as file:
        yield file.read()
