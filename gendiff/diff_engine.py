"""Module for contains diff engine."""
NESTED = 'nested'
CHANGED = 'changed'
UNCHANGED = 'unchanged'
REMOVED = 'removed'
ADDED = 'added'


def make_diff(data1: dict, data2: dict) -> dict:
    """Make row data using depth-first search."""
    diff = {}
    for key in data1.keys() & data2.keys():
        if isinstance(data1[key], dict) and isinstance(data2[key], dict):
            diff[key] = (NESTED, make_diff(data1[key], data2[key]))
        elif data1[key] != data2[key]:
            diff[key] = (CHANGED, (data1[key], data2[key]))
        else:
            diff[key] = (UNCHANGED, data2[key])
    for key in data1.keys() - data2.keys():
        diff[key] = (REMOVED, data1[key])
    for key in data2.keys() - data1.keys():
        diff[key] = (ADDED, data2[key])
    return diff
