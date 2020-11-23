import gendiff.generate_diff as gen_diff


def stringify(value):
    if isinstance(value, dict):
        value = '[complex value]'
    return value


def make_result(listing):
    result = []
    for (path, status, value) in listing:
        if status == gen_diff.NESTED:
            result.extend(value)

        elif status == gen_diff.REMOVED:
            string = f"Property '{path}' was {status}\n"
            result.append(string)

        elif status == gen_diff.ADDED:
            value = stringify(value)
            string = f"Property '{path}' was {status} with value: '{value}'\n"
            result.append(string)

        elif status == gen_diff.CHANGED:
            value_before, changed_value = value[0], value[1]
            value_before = stringify(value_before)
            changed_value = stringify(changed_value)
            string = f"Property '{path}' was updated. From '{value_before}' to '{changed_value}'\n"   # noqa: E501
            result.append(string)

    return result


def make_plain_text(diff):
    def inner(dict_tree, root_keys=None):
        output = []
        for key, (status, value) in sorted(dict_tree.items()):
            path = f'{root_keys}.{key}' if root_keys else key
            if status == gen_diff.NESTED:
                output.append((path, status, inner(value, path)))
            else:
                output.append((path, status, value))
        result = make_result(output)
        return ''.join(result)
    return inner(diff)
