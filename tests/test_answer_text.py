"""Testing mod."""
from gendiff.generate_diff import generate_diff

import pytest


def test_json(get_correct_diff_text):
    check_answer = generate_diff('tests/fixtures/file1.json',
                                 'tests/fixtures/file2.json')
    assert check_answer.split(
        '\n') == get_correct_diff_text, check_answer.split('\n')


def test_yaml(get_correct_diff_text):
    check_answer = generate_diff('tests/fixtures/file1.yaml',
                                 'tests/fixtures/file2.yaml')
    assert check_answer.split(
        '\n') == get_correct_diff_text, check_answer.split('\n')


@pytest.fixture
def get_correct_diff_text():
    with open('tests/fixtures/correct_diff_text') as file:
        yield file.read().splitlines()
