"""The main script."""

from gendiff import generate_diff
from gendiff.args import args


def main():
    """Print a help."""
    args
    diff = generate_diff(args.first_file, args.second_file)
    if args.format == 'plain':
        print(diff)


if __name__ == '__main__':
    main()
