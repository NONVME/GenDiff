from gendiff.formatters.json import make_json
from gendiff.formatters.plain import make_plain
from gendiff.formatters.stylish import make_pretty

PRETTY = 'pretty'
PLAIN = 'plain'
JSON = 'json'


def build(diff, format_type):
    if format_type == PRETTY:
        formatter = make_pretty(diff)
    elif format_type == JSON:
        formatter = make_json(diff)
    elif format_type == PLAIN:
        formatter = make_plain(diff)
    return formatter
