"""The argparse module for automatically generates help."""

import argparse
from gendiff.formatters.stylish import PRETTY, PLAIN, JSON
from gendiff import generate_diff


def get_args_parser():
    parser = argparse.ArgumentParser(
        description='Generate diff',
        prog='gendiff',
    )
    parser.add_argument('first_file', type=str)
    parser.add_argument('second_file', type=str)
    parser.add_argument('-f',
                        '--format',
                        help='\n set format of output',
                        choices=[PRETTY, PLAIN, JSON],
                        default=PRETTY,
                        type=str,
                        )

    return parser
