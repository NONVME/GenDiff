"""Module for create diff and formatting."""
import json
import os

import yaml
from gendiff.stylish import stylish


def generate_diff(file1: str, file2: str, format: str) -> str:
    """Generate diff between first and second dicts."""
    data1 = get_data(file1)
    data2 = get_data(file2)
    diff = make_diff(data1, data2)
    return stylish(diff, format)


def make_diff(data1: dict, data2: dict) -> dict:
    """Make row data using depth-first search."""
    diff = {}
    for key in data1.keys() & data2.keys():
        if isinstance(data1[key], dict) and isinstance(data2[key], dict):
            diff[key] = ('nested', make_diff(data1[key], data2[key]))
        elif data1[key] != data2[key]:
            diff[key] = ('changed', (data1[key], data2[key]))
        else:
            diff[key] = ('same', data2[key])
    for key in data1.keys() - data2.keys():
        diff[key] = ('removed', data1[key])
    for key in data2.keys() - data1.keys():
        diff[key] = ('added', data2[key])
    return diff


def get_data(path: str) -> dict:
    """Parse data from file to dict."""
    fullpath = os.path.abspath(path)
    _, ext = os.path.splitext(path)
    with open(fullpath, 'r', encoding='utf-8') as file:
        if ext.lower() in ('.yaml', '.yml'):
            return yaml.safe_load(file)
        return json.load(file)
