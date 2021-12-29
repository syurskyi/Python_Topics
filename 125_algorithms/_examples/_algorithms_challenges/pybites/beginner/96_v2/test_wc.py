from urllib.request import urlretrieve

import pytest

from wc import wc

lines = [b'Hello world',
         b'Keep calm and code in Python',
         b'Have a nice weekend']
py_file = 'https://bites-data.s3.us-east-2.amazonaws.com/driving.py'


@pytest.mark.parametrize("some_text, expected", [
    (lines[0], '1 2 11'),
    (b'\n'.join(lines[:2]), '2 8 40'),
    (b'\n'.join(lines), '3 12 60'),
])
def test_wc(some_text, expected, tmp_path):
    f = tmp_path / "some_file.txt"
    f.write_bytes(some_text)
    output = wc(f.resolve())
    # replace tabs / multiple spaces by single space
    counts = ' '.join(output.split()[:3])
    assert counts == expected
    # file with/without path allowed
    assert f.name in output


def test_wc_on_real_py_file(tmp_path):
    f = tmp_path / "driving.py"
    urlretrieve(py_file, f)
    output = wc(f.resolve())
    counts = ' '.join(output.split()[:3])
    # https://twitter.com/pybites/status/1175795375904628736
    expected = "7 29 216"  # not 8!
    assert counts == expected
    assert f.name in output
