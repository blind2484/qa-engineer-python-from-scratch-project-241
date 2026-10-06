def format_value(val):
    if isinstance(val, bool):
        return str(val).lower()
    if val is None:
        return 'null'
    return val