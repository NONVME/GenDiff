import gendiff.generate_diff as gen_diff


def stringify(value):
    string = ''
    if isinstance(value, dict):
        for index, value in value.items():
            string += '            {}: {}\n'.format(index, value)
        return '{{\n{}        }}'.format(string)
    return value


def text_prerender(diff):
    output = []
    for key, (status, value) in sorted(diff.items()):
        if status == gen_diff.NESTED:
            output.append('    {}: {{\n    {}\n    }}'.format(
                key, text_prerender(value)))
        elif status == gen_diff.NO_CHANGED:
            output.append('    {}: {}'.format(key, stringify(value)))
        elif status == gen_diff.CHANGED:
            old, new = value
            output.append('  - {}: {}'.format(key, stringify(old)))
            output.append('  + {}: {}'.format(key, stringify(new)))
        elif status == gen_diff.REMOVED:
            output.append('  - {}: {}'.format(key, stringify(value)))
        elif status == gen_diff.ADDED:
            output.append('  + {}: {}'.format(key, stringify(value)))
    return '\n    '.join(output)


def make_pretty_text(diff):
    return '{{\n{}\n}}'.format(text_prerender(diff))
