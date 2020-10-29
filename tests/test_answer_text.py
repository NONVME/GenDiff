import pytest

from gendiff.generate_diff import generate_diff, get_data


def test_answer(correct_plain_diff):
    check_answer = generate_diff('tests/fixtures/file1.json',
                                 'tests/fixtures/file2.json')
    assert check_answer.split('\n') == correct_plain_diff


@pytest.fixture
def correct_plain_diff():
    with open('tests/fixtures/correct_diff_text') as file:
        yield file.read().splitlines()
