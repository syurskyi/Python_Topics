_______ filecmp
____ urllib.request _______ urlretrieve

_______ pytest

____ get_my_code _______ get_passing_code, url, tmp


@pytest.mark.parametrize('actual_filename, expected_filename', [
    ('Bite01.py', 'Bite01_Expected.py'),
    ('Bite02.py', 'Bite02_Expected.py')
])
___ test_compare_files(actual_filename, expected_filename):
    actual = tmp / actual_filename
    expected = tmp / expected_filename
    get_passing_code()
    urlretrieve(url.f..(filename=expected_filename),
                expected)
    ... filecmp.cmp(actual, expected)