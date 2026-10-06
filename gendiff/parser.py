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