"""The argparse module for automatically generates help."""

import argparse

parser = argparse.ArgumentParser(
    description='Generate diff',
    prog='gendiff',
)
parser.add_argument('first_file', type=str)
parser.add_argument('second_file', type=str)
parser.add_argument('-f',
                    '--format',
                    help='\n set format of output',
                    choices=['plain', 'json'],
                    default='plain',
                    type=str)

args = parser.parse_args()
