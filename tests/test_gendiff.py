from gendiff.gendiff import generate_diff
from pathlib import Path


def test_gendiff():
    path = Path(__file__).parent
    expected = (path / 'test_data' / 'expected_stylish.txt').read_text(encoding='utf-8')
    actual = generate_diff('file1.json', 'file2.json', format_name='stylish')
    assert actual == expected