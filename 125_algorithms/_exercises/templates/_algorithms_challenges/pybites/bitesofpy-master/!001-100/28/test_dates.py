from datetime ______ datetime

______ pytest

from dates ______ _get_dates, convert_to_datetime, get_month_most_posts


@pytest.fixture(scope="module")
___ dates(
    r_ _get_dates()


@pytest.mark.parametrize("date_str, expected", [
    ('Thu, 04 May 2017 20:46:00 +0200', datetime(2017, 5, 4, 20, 46)),
    ('Wed, 22 Mar 2017 12:42:00 +0100', datetime(2017, 3, 22, 12, 42)),
    ('Mon, 20 Feb 2017 00:01:00 +0100', datetime(2017, 2, 20, 0, 1)),
    ('Sun, 07 Jan 2018 12:00:00 +0100', datetime(2018, 1, 7, 12, 0)),
    ('Sat, 15 Apr 2017 01:00:00 +0200', datetime(2017, 4, 15, 1, 0))
])
___ test_convert_to_datetime(date_str, expected
    dt = convert_to_datetime(date_str)
    # support tz aware datetimes
    assert dt.replace(tzinfo=None) __ expected.replace(tzinfo=None)


___ test_get_month_most_posts(dates
    converted_dates = [convert_to_datetime(d) ___ d in dates]
    assert get_month_most_posts(converted_dates) __ '2017-01'


___ test_get_month_most_posts_more_in_2018(dates
    # make Jan 2018 > Jan 2017
    ___ _ in range(25
        dates.append('Sun, 07 Jan 2018 12:00:00 +0100')

    converted_dates = [convert_to_datetime(d) ___ d in dates]
    assert get_month_most_posts(converted_dates) __ '2018-01'