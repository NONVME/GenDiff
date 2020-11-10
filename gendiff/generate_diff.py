"""Module for create diff and formatting."""
import json
import os
from collections import OrderedDict
from pprint import pp, pprint

import yaml


def generate_diff(file1: str, file2: str) -> str:
    """Generate diff between first and second dicts."""
    data1 = get_data(file1)
    data2 = get_data(file2)
    diff = make_diff(data1, data2)
    return render_to_text(diff)
    # return render_to_json(diff)


def make_diff(data1: dict, data2: dict) -> dict:
    """Make row data using depth-first search."""
    # Нужно проходиться по ключам значения котоорых словари
    d1_keys = set(data1.keys())
    d2_keys = set(data2.keys())

    intersect_keys = d1_keys.intersection(d2_keys)
    intersect_keys = sorted(list(intersect_keys))

    # print('d1_keys: ', d1_keys)
    # print('d2_keys: ', d2_keys)
    # print('intersect: ', intersect_keys)

    for i in intersect_keys:
        if isinstance(data1[i], dict) and isinstance(data2[i], dict):
            new_diff = list(map(lambda x: make_diff(data1[x], data2[x]), intersect_keys))
        # return new_diff
        same = {o: data1[o] for o in intersect_keys if data1[o] == data2[o]}
        removed = {o: data1[o] for o in d1_keys - d2_keys}
        mod_removed = {o: data1[o] for o in intersect_keys if data1[o] != data2[o]}
        mod_added = {o: data2[o] for o in intersect_keys if data1[o] != data2[o]}
        added = {o: data2[o] for o in d2_keys - d1_keys}

        # make_diff(data1[intersect_keys], data2[intersect_keys])
        diff = {
            'blank': {
                **sort_dict(same)
            },
            'minus': {
                **sort_dict(removed),
                **sort_dict(mod_removed)
            },
            'plus': {
                **sort_dict(mod_added),
                **sort_dict(added)
            }
        }

        return diff


def sort_dict(row_dict: dict):
    """Sort dict for normilize the diff."""
    return OrderedDict(sorted(row_dict.items(), key=lambda x: x[0]))


def get_data(path: str) -> dict:
    """Parse data from file to dict."""
    fullpath = os.path.abspath(path)
    _, ext = os.path.splitext(path)
    with open(fullpath, 'r', encoding='utf-8') as file:
        if ext.lower() in ('.yaml', '.yml'):
            return yaml.safe_load(file)
        return json.load(file)


def render_to_text(diff: dict) -> str:
    """Format diff dict to plain text."""
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
        diff.update({field: strings})
    return '{{\n{blank}\n{minus}\n{plus}\n}}'.format(**diff)


def render_to_json(diff: dict) -> str:
    return json.dumps(diff, indent=2)

