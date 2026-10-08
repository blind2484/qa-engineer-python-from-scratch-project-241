from pathlib import Path

from gendiff.gendiff import generate_diff

path = Path(__file__).parent
file1_json = path / 'test_data' / 'file1.json'
file2_json = path / 'test_data' / 'file2.json'
file1_yaml = path / 'test_data' / 'file1.yml'
file2_yaml = path / 'test_data' / 'file2.yml'


def test_gendiff_json_stylish():
    expected = (
        path / 'test_data' / 'expected_stylish.txt'
    ).read_text(encoding='utf-8')
    actual = generate_diff(file1_json, file2_json, format_name='stylish')
    assert actual == expected


def test_gendiff_yaml_stylish():
    expected = (
        path / 'test_data' / 'expected_stylish.txt'
    ).read_text(encoding='utf-8')
    actual = generate_diff(file1_yaml, file2_yaml)
    assert actual == expected


def test_gendiff_plain():
    expected = (
        path / 'test_data' / 'expected_plain.txt'
    ).read_text(encoding='utf-8')
    actual = generate_diff(file1_yaml, file2_json, format_name='plain')
    assert actual == expected


def test_gendiff_json():
    expected = (
        path / 'test_data' / 'expected_json.json'
    ).read_text(encoding='utf-8')
    actual = generate_diff(file1_yaml, file2_json, format_name='json')
    assert actual == expected