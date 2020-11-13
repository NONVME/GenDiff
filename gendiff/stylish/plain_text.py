def change_value_to_complex(value):
    if isinstance(value, dict):
        value = '[complex value]'
    return value


def make_result(list):
    result = []
    for (path, status, value) in list:
        if status == 'nested':
            result.extend(value)

        if status == 'removed':
            string = f"Property '{path}' was {status}\n"
            result.append(string)

        elif status == 'added':
            value = change_value_to_complex(value)
            string = f"Property '{path}' was {status} with value: '{value}'\n"
            result.append(string)

        elif status == 'changed':
            value_before, changed_value = value[0], value[1]
            value_before = change_value_to_complex(value_before)
            changed_value = change_value_to_complex(changed_value)
            string = f"Property '{path}' was updated. From " \
                     f"'{value_before}' to '{changed_value}'\n"
            result.append(string)

    return result


def make_plain_text(diff):
    def inner(dictionary, root_keys=None):
        strings = []
        for key, (status, value) in dictionary.items():
            path = f"{root_keys}.{key}" if root_keys else key
            if status == 'nested':
                strings.append([path, status, inner(value, path)])
            else:
                strings.append((path, status, value))

        strings = list(map(list, strings))
        strings.sort()
        result = (make_result(strings))
        return "".join(result)
    return inner(diff)
