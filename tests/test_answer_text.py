import pytest

from gendiff.generate_diff import generate_diff, get_data


def test_answer(get_correct_diff_text):
    check_answer = generate_diff('tests/fixtures/file1.json',
                                 'tests/fixtures/file2.json')
    assert check_answer.split('\n') == get_correct_diff_text, check_answer.split('\n')


@pytest.fixture
def get_correct_diff_text():
    with open('tests/fixtures/correct_diff_text') as file:
        yield file.read().splitlines()
