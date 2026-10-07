from gendiff.formatters.format_value import format_value


def to_plain(result_data):
    out = ''
    for key in result_data:
        old_val = format_value(result_data[key].get('old_value'))
        new_val = format_value(result_data[key].get('new_value'))
        if result_data.get(key).get('status') == 'removed':
            out += f"Property '{key}' was removed\n"
        elif result_data.get(key).get('status') == 'added':
            out += f"Property '{key}' was added with value: {new_val}\n"
        elif result_data.get(key).get('status') == 'updated':
            out += f"Property '{key}' was updated. " \
                f"From {old_val} to {new_val}\n"
    return out[:-1]