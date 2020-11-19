from gendiff.formatters.json import make_json
from gendiff.formatters.plain_text import make_plain_text
from gendiff.formatters.pretty_text import make_pretty_text

PRETTY = 'pretty'
PLAIN = 'plain'
JSON = 'json'


def stylish(diff, format_type=PRETTY):
    if format_type == PRETTY:
        formatter = make_pretty_text(diff)
    elif format_type == JSON:
        formatter = make_json(diff)
    else:
        formatter = make_plain_text(diff)
    return formatter
