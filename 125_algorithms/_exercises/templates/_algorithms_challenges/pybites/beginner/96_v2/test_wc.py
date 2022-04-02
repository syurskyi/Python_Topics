____ urllib.request _______ urlretrieve

_______ p__

____ wc _______ wc

lines = [b'Hello world',
         b'Keep calm and code in Python',
         b'Have a nice weekend'
py_file = 'https://bites-data.s3.us-east-2.amazonaws.com/driving.py'


?p__.m__.p.("some_text, expected", [
    (lines[0], '1 2 11'),
    (b'\n'.j..(lines[:2]), '2 8 40'),
    (b'\n'.j..(lines), '3 12 60'),
])
___ test_wc(some_text, expected, tmp_path
    f = tmp_path / "some_file.txt"
    f.w..(some_text)
    output = wc(f.resolve())
    # replace tabs / multiple spaces by single space
    counts = ' '.j..(output.s.. [:3])
    ... counts __ expected
    # file with/without path allowed
    ... f.name __ output


___ test_wc_on_real_py_file(tmp_path
    f = tmp_path / "driving.py"
    urlretrieve(py_file, f)
    output = wc(f.resolve())
    counts = ' '.j..(output.s.. [:3])
    # https://twitter.com/pybites/status/1175795375904628736
    expected = "7 29 216"  # not 8!
    ... counts __ expected
    ... f.name __ output
