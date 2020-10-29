"""Module for create diff and formatting."""
import json
import os


def get_data(path: str) -> dict:
    """Parse data from file to dict."""
    fullpath = os.path.abspath(path)
    with open(fullpath, 'r') as file:
        return json.load(file)


def get_plain(blank: list, minus: list, plus: list) -> str:
    """Format diff dict to plain text."""
    return '{{\n{0}\n{1}\n{2}\n}}'.format(unpack(blank),
                                          unpack(minus),
                                          unpack(plus))


def unpack(listing: list) -> str:
    return '\n'.join((sum(listing, [])))


def generate_diff(file1: str, file2: str) -> str:
    """Generate diff between first and second dicts."""
    data1 = get_data(file1)
    data2 = get_data(file2)
    same, removed, modified_del, modified_add, added = make_diff(data1, data2)
    blank = []
    minus = []
    plus = []
    for key, value in {**same}.items():
        blank.append(['   ' + str(key) + ': ' + str(value)])
    for key, value in {**removed, **modified_del}.items():
        minus.append([' - ' + str(key) + ': ' + str(value)])
    for key, value in {**modified_add, **added}.items():
        plus.append([' + ' + str(key) + ': ' + str(value)])
    return get_plain(blank, minus, plus)


def make_diff(data1: dict, data2: dict) -> dict:
    d1_keys = set(data1.keys())
    d2_keys = set(data2.keys())
    intersect_keys = d1_keys.intersection(d2_keys)

    same = {o: data1[o] for o in intersect_keys if data1[o] == data2[o]}
    removed = {o: data1[o] for o in d1_keys - d2_keys}
    mod_removed = {o: data1[o] for o in intersect_keys if data1[o] != data2[o]}
    mod_added = {o: data2[o] for o in intersect_keys if data1[o] != data2[o]}
    added = {o: data2[o] for o in d2_keys - d1_keys}
    return same, removed, mod_removed, mod_added, added
