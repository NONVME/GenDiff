"""The argparse module for automatically generates help."""

import argparse

from gendiff.formatters.format import FORMATTERS


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
                        choices=sorted(FORMATTERS.keys()),
                        default=FORMATTERS.keys()[0],
                        type=str,
                        )

    return parser
