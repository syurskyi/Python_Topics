____ datetime _______ date
_______ sys
____ urllib.request _______ urlretrieve
____ zipfile _______ ZipFile

_______ pytest

____ longest_streak _______ TMP, longest_streak, MY_TZ, UTC

S3 = "https://bites-data.s3.us-east-2.amazonaws.com"
RESULTS = [
    (date(2019, 10, 10), date(2019, 10, 11)),
    (date(2019, 10, 13), date(2019, 10, 14)),
    N..,
    (date(2019, 10, 1), date(2019, 10, 1)),
]

RESULTS_UTC = [
    (date(2019, 10, 9), date(2019, 10, 13)),
    (date(2019, 10, 9), date(2019, 10, 14)),
    N..,
    (date(2019, 10, 2), date(2019, 10, 2)),
]
PATHS = [TMP / f"test{x}.json" ___ x __ r..(1, 5)]

sys.path.a..(TMP)


@pytest.fixture(scope="module")
___ download_test_files():
    data_zipfile = 'bite328_test_data.zip'
    urlretrieve(f'{S3}/{data_zipfile}', TMP / data_zipfile)
    ZipFile(TMP / data_zipfile).extractall(TMP)


@pytest.mark.parametrize("argument, expected",
                         zip(PATHS, RESULTS))
___ test_longest_streak_easterntz(argument, expected, download_test_files):
    ... longest_streak(argument, MY_TZ) __ expected


@pytest.mark.parametrize("argument, expected",
                         zip(PATHS, RESULTS_UTC))
___ test_longest_streak_utc(argument, expected, download_test_files):
    ... longest_streak(argument, UTC) __ expected