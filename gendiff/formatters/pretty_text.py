import gendiff.generate_diff as gen_diff


def make_pretty_text(diff):
    def inner(dictionary, space=2):
        strings = []
        for key, value in sorted(dictionary.items()):
            if isinstance(value, dict):
                strings.append(
                    (key, gen_diff.NESTED, inner(value, space=space + 4)))
            elif not isinstance(value, tuple):
                strings.append((key, gen_diff.NESTED, value))
            elif isinstance(value[1], dict):
                strings.append((key, value[0], inner(value[1],
                                                     space=space + 4)))
            elif isinstance(value[1], tuple) and isinstance(value[1][0], dict):
                strings.append(
                    (key, value[0], (inner(value[1][0],
                                           space=space + 4), value[1][1])))
            elif isinstance(value[1], tuple) and isinstance(value[1][1], dict):
                strings.append(
                    (key, value[0], (inner(value[1][1],
                                           space=space + 4), value[1][0])))
            else:
                strings.append((key, value[0], value[1]))
        result = text_prerender(strings, space)
        return '\n'.join(result)
    return inner(diff)


def text_prerender(diff, space):
    spaces = ' ' * space
    output = ['{']
    for key, status, value in diff:

        if status == gen_diff.NESTED:
            output.append('{}  {}: {}'.format(spaces, key, value))
        elif status == gen_diff.NO_CHANGED:
            output.append('{}  {}: {}'.format(spaces, key, value))
        elif status == gen_diff.CHANGED:
            old, new = value
            output.append('{}- {}: {}'.format(spaces, key, old))
            output.append('{}+ {}: {}'.format(spaces, key, new))
        elif status == gen_diff.REMOVED:
            output.append('{}- {}: {}'.format(spaces, key, value))
        elif status == gen_diff.ADDED:
            output.append('{}+ {}: {}'.format(spaces, key, value))
    output.append(' ' * (space - 2) + '}')
    return output
