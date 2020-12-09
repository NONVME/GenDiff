from gendiff.formatters.json import make_json
from gendiff.formatters.plain import make_plain
from gendiff.formatters.stylish import make_pretty

PRETTY = 'pretty'
PLAIN = 'plain'
JSON = 'json'

format = {
    PRETTY: make_pretty,
    PLAIN: make_plain,
    JSON: make_json,
}


def build(diff, format_type):
    try:
        if format_type in format:
            formatter = format[format_type](diff)
        else:
            raise Exception('No such formatter')
        return formatter
    except Exception as e:
        print('Exception: ' + str(e))
