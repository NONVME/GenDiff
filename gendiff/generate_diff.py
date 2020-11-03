"""Module for create diff and formatting."""
import json
import os
from collections import OrderedDict

import yaml


def generate_diff(file1: str, file2: str) -> str:
    """Generate diff between first and second dicts."""
    data1 = get_data(file1)
    data2 = get_data(file2)
    diff = make_diff(data1, data2)
    return gen_plain_text(diff)


def make_diff(data1: dict, data2: dict) -> dict:
    """Make row date."""
    d1_keys = set(data1.keys())
    d2_keys = set(data2.keys())
    intersect_keys = d1_keys.intersection(d2_keys)

    same = {o: data1[o] for o in intersect_keys if data1[o] == data2[o]}
    removed = {o: data1[o] for o in d1_keys - d2_keys}
    mod_removed = {o: data1[o] for o in intersect_keys if data1[o] != data2[o]}
    mod_added = {o: data2[o] for o in intersect_keys if data1[o] != data2[o]}
    added = {o: data2[o] for o in d2_keys - d1_keys}

    return {'blank': {**sort_dict(same)},
            'minus': {**sort_dict(removed), **sort_dict(mod_removed)},
            'plus': {**sort_dict(mod_added), **sort_dict(added)}}


def sort_dict(row_dict: dict):
    """Sort dict for normilize the diff."""
    return OrderedDict(sorted(row_dict.items(), key=lambda x: x[0]))


def get_data(path: str) -> dict:
    """Parse data from file to dict."""
    fullpath = os.path.abspath(path)
    _, ext = os.path.splitext(path)
    with open(fullpath, 'r', encoding='utf-8') as file:
        if ext == '.json':
            return json.load(file)
        elif ext == '.yaml':
            return yaml.safe_load(file)
        elif ext == '.yml':
            return yaml.safe_load(file)


def gen_plain_text(diff: dict) -> str:
    """Format diff dict to plain text."""
    diff_copy = diff.copy()
    for field, inner_dict in diff.items():
        key = inner_dict.keys()
        value = inner_dict.values()
        if field == 'blank':
            strings = '\n'.join(
                ['   ' + str(a) + ': ' + str(b) for a, b in zip(key, value)])
        if field == 'minus':
            strings = '\n'.join(
                [' - ' + str(a) + ': ' + str(b) for a, b in zip(key, value)])
        if field == 'plus':
            strings = '\n'.join(
                [' + ' + str(a) + ': ' + str(b) for a, b in zip(key, value)])
        diff_copy.update({field: strings})
    return '{{\n{blank}\n{minus}\n{plus}\n}}'.format(**diff_copy)
