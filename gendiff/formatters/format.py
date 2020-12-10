from gendiff.formatters.json import make_json
from gendiff.formatters.plain import make_plain
from gendiff.formatters.stylish import make_pretty

PRETTY = 'pretty'
PLAIN = 'plain'
JSON = 'json'

FORMATTERS = {
    PRETTY: make_pretty,
    PLAIN: make_plain,
    JSON: make_json,
}


def build(diff, format_type):
    try:
        formatter = FORMATTERS[format_type]
    except KeyError:
        raise ValueError(f'No such formatter {format_type}')
    else:
        return formatter(diff)
