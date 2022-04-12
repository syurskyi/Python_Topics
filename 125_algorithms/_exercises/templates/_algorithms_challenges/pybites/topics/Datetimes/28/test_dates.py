____ d__ _______ d__

_______ p__

____ dates _______ _get_dates, convert_to_datetime, get_month_most_posts


?p__.f..(scope="module")
___ dates
    r.. _get_dates()


?p__.m__.p.("date_str, expected", [
    ('Thu, 04 May 2017 20:46:00 +0200', d__(2017, 5, 4, 20, 46,
    ('Wed, 22 Mar 2017 12:42:00 +0100', d__(2017, 3, 22, 12, 42,
    ('Mon, 20 Feb 2017 00:01:00 +0100', d__(2017, 2, 20, 0, 1,
    ('Sun, 07 Jan 2018 12:00:00 +0100', d__(2018, 1, 7, 12, 0,
    ('Sat, 15 Apr 2017 01:00:00 +0200', d__(2017, 4, 15, 1, 0
])
___ test_convert_to_datetime date_str e..
    dt convert_to_datetime date_str)
    # support tz aware datetimes
    ... dt.r.. t.._N.. __ e...r.. t.._N..


___ test_get_month_most_posts dates
    converted_dates  c.. d ___ ? __ ?
    ... ? ? __ '2017-01'


___ test_get_month_most_posts_more_in_2018(dates
    # make Jan 2018 > Jan 2017
    ___ _ __ r..(25
        dates.a..('Sun, 07 Jan 2018 12:00:00 +0100')

    converted_dates  c.. d ___ ? __ ?
    ... ? ? __ '2018-01'
