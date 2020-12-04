import gendiff.diff_engine as diff_engine


def stringify(value):
    if isinstance(value, dict):
        value = '[complex value]'
    return value


def make_plain(diff):
    def inner(dict_tree, root_keys=None):
        output = []
        for key, (status, value) in sorted(dict_tree.items()):
            path = f'{root_keys}.{key}' if root_keys else key
            if status == diff_engine.NESTED:
                output.append((path, status, inner(value, path)))
            else:
                output.append((path, status, value))
        result = make_result(output)
        return '\n'.join(result)
    return inner(diff)


def make_result(listing):
    result = []
    for (path, status, value) in listing:
        if status == diff_engine.NESTED:
            result.append(value)

        elif status == diff_engine.REMOVED:
            string = f"Property '{path}' was {status}"
            result.append(string)

        elif status == diff_engine.ADDED:
            value = stringify(value)
            string = f"Property '{path}' was {status} with value: '{value}'"
            result.append(string)

        elif status == diff_engine.CHANGED:
            value_before, changed_value = map(stringify, value)
            string = f"Property '{path}' was updated. From '{value_before}' to '{changed_value}'"   # noqa: E501
            result.append(string)

    return result
