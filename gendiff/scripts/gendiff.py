"""The main script."""

from gendiff import generate_diff
from gendiff.args import get_args_parser


def main():
    """Select format selection."""
    args = get_args_parser().parse_args()
    print(generate_diff(args.first_file, args.second_file, args.format))


if __name__ == '__main__':
    main()
