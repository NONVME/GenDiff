def dict2string(dictionary_or_str):
    string = ''
    if isinstance(dictionary_or_str, dict):
        for index, value in dictionary_or_str.items():
            string += "            {}: {}\n".format(index, value)
        return "{{\n{}        }}".format(string)
    return dictionary_or_str


def text_prerender(diff):
    list_of_str = []
    for key, (status, value) in sorted(diff.items()):
        if status == 'nested':
            list_of_str.append("    {}: {{\n    {}\n    }}".format(key, text_prerender(value))) # noqa E501
        elif status == 'same':
            list_of_str.append("    {}: {}".format(key, dict2string(value)))
        elif status == 'changed':
            old, new = value
            list_of_str.append("  - {}: {}".format(key, dict2string(old)))
            list_of_str.append("  + {}: {}".format(key, dict2string(new)))
        elif status == 'removed':
            list_of_str.append("  - {}: {}".format(key, dict2string(value)))
        elif status == 'added':
            list_of_str.append("  + {}: {}".format(key, dict2string(value)))
    return '\n    '.join(list_of_str)


def make_prety_text(diff):
    return "{{\n{}\n}}".format(text_prerender(diff))
