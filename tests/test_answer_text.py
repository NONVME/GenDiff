"""Testing mod."""
import json

import pytest
from gendiff.diff_generator import generate_diff
from gendiff.formatters.stylish import JSON, PLAIN, PRETTY

JSON_FILE1 = 'tests/fixtures/file1.json'
JSON_FILE2 = 'tests/fixtures/file2.json'
YAML_FILE1 = 'tests/fixtures/file1.yaml'
YAML_FILE2 = 'tests/fixtures/file2.yaml'


def test_pretty(pretty_validation):
    assert generate_diff(JSON_FILE1, JSON_FILE2, PRETTY) == pretty_validation
    assert generate_diff(YAML_FILE1, YAML_FILE2, PRETTY) == pretty_validation


def test_plain(plain_validation):
    assert generate_diff(JSON_FILE1, JSON_FILE2, PLAIN) == plain_validation
    assert generate_diff(YAML_FILE1, YAML_FILE2, PLAIN) == plain_validation


def test_json(json_validation):
    input_json = generate_diff(JSON_FILE1, JSON_FILE2, JSON)
    input_yaml = generate_diff(YAML_FILE1, YAML_FILE2, JSON)
    assert json.loads(input_json) == json.loads(json_validation)
    assert json.loads(input_yaml) == json.loads(json_validation)


@pytest.fixture
def pretty_validation():
    with open('tests/fixtures/correct_pretty') as file:
        yield file.read()


@pytest.fixture
def plain_validation():
    with open('tests/fixtures/correct_plain') as file:
        yield file.read()


@pytest.fixture
def json_validation():
    with open('tests/fixtures/correct_json') as file:
        yield file.read()
