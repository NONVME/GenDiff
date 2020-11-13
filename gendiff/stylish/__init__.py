from gendiff.stylish.json import make_json
from gendiff.stylish.plain_text import make_plain_text
from gendiff.stylish.prety_text import make_prety_text


def stylish(diff, format_type):
    if format_type == 'prety':
        return make_prety_text(diff)
    elif format_type == 'json':
        return make_json(diff)
    elif format_type == 'plain':
        return make_plain_text(diff)
