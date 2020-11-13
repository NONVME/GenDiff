"""The main script."""

from gendiff import generate_diff
from gendiff.args import args


def main():
    """Selection format selection."""
    args
    print(generate_diff(args.first_file, args.second_file, args.format))


if __name__ == '__main__':
    main()
