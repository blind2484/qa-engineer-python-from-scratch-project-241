from gendiff.formatters.format_value import format_value


def to_stylish(result_data):
    out = '{\n'
    for key in result_data:
        value = format_value(result_data[key].get('value'))
        old_val = format_value(result_data[key].get('old_value'))
        new_val = format_value(result_data[key].get('new_value'))
        if result_data.get(key).get('status') == 'unchanged':
            out += f'    {key}: {value}\n'
        elif result_data.get(key).get('status') == 'removed':
            out += f'  - {key}: {old_val}\n'
        elif result_data.get(key).get('status') == 'added':
            out += f'  + {key}: {new_val}\n'
        elif result_data.get(key).get('status') == 'updated':
            out += f'  - {key}: {old_val}\n  + {key}: {new_val}\n'
    out += '}'
    return out