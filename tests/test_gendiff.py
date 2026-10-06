from pathlib import Path

from gendiff.gendiff import generate_diff


def test_gendiff_json_stylish():
    path = Path(__file__).parent
    expected = (
        path / 'test_data' / 'expected_stylish.txt'
    ).read_text(encoding='utf-8')
    actual = generate_diff('file1.json', 'file2.json', format_name='stylish')
    assert actual == expected


def test_gendiff_yaml_stylish():
    path = Path(__file__).parent
    expected = (
        path / 'test_data' / 'expected_stylish.txt'
    ).read_text(encoding='utf-8')
    actual = generate_diff('file1.yml', 'file2.yml')
    assert actual == expected