import json
from pathlib import Path
import yaml


def parse_file_to_dict(file):
    ext = Path(file).suffix.lstrip(".").lower()
    with open(file, "r", encoding="utf-8") as f:
        if ext == "json":
            data = json.load(f)
        elif ext in ["yaml", "yml"]:
            data = yaml.safe_load(f)
        else:
            raise ValueError('Неподдерживаемый формат')
    return data


def compare_dicts(first_file, second_file):
    first_data = parse_file_to_dict(first_file)
    second_data = parse_file_to_dict(second_file)
    result_data = {}
    
    keys1 = set(first_data.keys())
    keys2 = set(second_data.keys())

    only_in_first = keys1 - keys2
    for key in only_in_first:
        result_data.update({key: {'status': 'removed',
                                  'old_value': first_data[key]}})
    only_in_second = keys2 - keys1
    for key in only_in_second:
        result_data.update({key: {'status': 'added',
                                  'new_value': second_data[key]}})

    common_keys = keys1 & keys2
    for key in common_keys:
        if first_data[key] != second_data[key]:
            result_data.update({key: {'status': 'updated',
                                      'old_value': first_data[key],
                                      'new_value': second_data[key]}})
        else:
            result_data.update({key: {'status': 'unchanged',
                                      'value': first_data[key]}})

    result_data = {key: result_data[key] for key in sorted(result_data)}
    return result_data


def formatter(result_data):
    out = '{\n'
    for key in result_data:
        def to_lower(val):
            if isinstance(val, bool):
                return str(val).lower()
            return val.lower() if isinstance(val, str) else val
        value = to_lower(result_data[key].get('value'))
        old_val = to_lower(result_data[key].get('old_value'))
        new_val = to_lower(result_data[key].get('new_value'))
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


def generate_diff(first_file, second_file, format_name):
    diff_data = compare_dicts(first_file, second_file)
    formatted_output = formatter(diff_data)
    return formatted_output