"""Testing mod."""
from gendiff.generate_diff import generate_diff

import pytest


def test_pretty_mini_json(get_correct_pretty_mini):
    check_answer = generate_diff('tests/fixtures/file1.json',
                                 'tests/fixtures/file2.json',
                                 'pretty')
    assert check_answer.split(
        '\n') == get_correct_pretty_mini, check_answer.split('\n')


def test_pretty_mini_yaml(get_correct_pretty_mini):
    check_answer = generate_diff('tests/fixtures/file1.yaml',
                                 'tests/fixtures/file2.yaml',
                                 'pretty')
    assert check_answer.split(
        '\n') == get_correct_pretty_mini, check_answer.split('\n')


def test_pretty(get_correct_pretty):
    check_answer = generate_diff('tests/fixtures/deep_file1.json',
                                 'tests/fixtures/deep_file2.json',
                                 'pretty')
    assert check_answer.split(
        '\n') == get_correct_pretty, check_answer.split('\n')


def test_plain(get_correct_plain):
    check_answer = generate_diff('tests/fixtures/deep_file1.json',
                                 'tests/fixtures/deep_file2.json',
                                 'plain')
    assert check_answer.split(
        '\n') == get_correct_plain, check_answer.split('\n')


def test_json(get_correct_json):
    check_answer = generate_diff('tests/fixtures/deep_file1.json',
                                 'tests/fixtures/deep_file2.json',
                                 'json')
    assert check_answer.split('\n') == get_correct_json, check_answer.split(
        '\n')


@pytest.fixture
def get_correct_pretty_mini():
    with open('tests/fixtures/correct_pretty_mini') as file:
        yield file.read().splitlines()


@pytest.fixture
def get_correct_pretty():
    with open('tests/fixtures/correct_pretty') as file:
        yield file.read().splitlines()


@pytest.fixture
def get_correct_plain():
    with open('tests/fixtures/correct_plain') as file:
        yield file.read().splitlines()


@pytest.fixture
def get_correct_json():
    with open('tests/fixtures/correct_json') as file:
        yield file.read().splitlines()
