import json


def to_json(result_data):
    out = {}
    for key in result_data:
        value = result_data[key].get('value')
        old_val = result_data[key].get('old_value')
        new_val = result_data[key].get('new_value')
        if result_data.get(key).get('status') == 'unchanged':
            out[key] = value
        elif result_data.get(key).get('status') == 'removed':
            out[key] = {"-": old_val}
        elif result_data.get(key).get('status') == 'added':
            out[key] = {"+": new_val}
        elif result_data.get(key).get('status') == 'updated':
            out[key] = {"-": old_val,
                        "+": new_val}
    return json.dumps(out, indent=2, ensure_ascii=False)