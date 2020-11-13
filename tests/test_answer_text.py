"""Testing mod."""
from gendiff.generate_diff import generate_diff

import pytest


def test_prety_mini_json(get_correct_prety_mini):
    check_answer = generate_diff('tests/fixtures/file1.json',
                                 'tests/fixtures/file2.json',
                                 'prety')
    assert check_answer.split(
        '\n') == get_correct_prety_mini, check_answer.split('\n')


def test_prety_mini_yaml(get_correct_prety_mini):
    check_answer = generate_diff('tests/fixtures/file1.yaml',
                                 'tests/fixtures/file2.yaml',
                                 'prety')
    assert check_answer.split(
        '\n') == get_correct_prety_mini, check_answer.split('\n')


def test_prety(get_correct_prety):
    check_answer = generate_diff('tests/fixtures/deep_file1.json',
                                 'tests/fixtures/deep_file2.json',
                                 'prety')
    assert check_answer.split(
        '\n') == get_correct_prety, check_answer.split('\n')


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
    assert check_answer.split(
        '\n') == get_correct_json, check_answer.split('\n')


@pytest.fixture
def get_correct_prety_mini():
    with open('tests/fixtures/correct_prety_mini') as file:
        yield file.read().splitlines()


@pytest.fixture
def get_correct_prety():
    with open('tests/fixtures/correct_prety') as file:
        yield file.read().splitlines()


@pytest.fixture
def get_correct_plain():
    with open('tests/fixtures/correct_plain') as file:
        yield file.read().splitlines()


@pytest.fixture
def get_correct_json():
    with open('tests/fixtures/correct_json') as file:
        yield file.read().splitlines()
