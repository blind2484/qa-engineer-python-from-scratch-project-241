from gendiff.formatters.plain import plain
from gendiff.formatters.stylish import stylish
from gendiff.parser import parse_file_to_dict


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


def formatter(result_data, format_name):
    if format_name == 'stylish':
        return stylish(result_data)
    if format_name == 'plain':
        return plain(result_data)
    raise ValueError(f"Unknown output format: '{format_name}'")


def generate_diff(first_file, second_file, format_name='stylish'):
    diff_data = compare_dicts(first_file, second_file)
    formatted_output = formatter(diff_data, format_name)
    return formatted_output