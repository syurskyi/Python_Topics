_______ d__

____ streak _______ extract_dates, calculate_streak


___ test_extract_dates
    data """
    +------------+------------+---------+
    | date       | activity   | count   |
    |------------+------------+---------|
    | 2018-11-10 | pcc        | 1       |
    | 2018-11-09 | 100d       | 1       |
    | 2018-11-07 | 100d       | 2       |
    | 2018-10-23 | pcc        | 1       |
    | 2018-10-15 | pcc        | 1       |
    | 2018-10-05 | bite       | 1       |
    | 2018-09-21 | bite       | 4       |
    | 2018-09-18 | bite       | 2       |
    | 2018-09-18 | bite       | 4       |
    +------------+------------+---------+
    """
    dates extract_dates(data)
    ... l..(dates) __ 8  # one less = deduped 2018-09-18
    ... d__.date(2018, 9, 18) __ dates
    ... d__.date(2018, 10, 23) __ dates
    ... d__.date(2018, 11, 9) __ dates


___ test_streak_of_0_days
    data """
    +------------+------------+---------+
    | date       | activity   | count   |
    |------------+------------+---------|
    | 2018-11-10 | pcc        | 1       |
    | 2018-11-09 | 100d       | 1       |
    | 2018-11-07 | 100d       | 2       |
    | 2018-10-23 | pcc        | 1       |
    | 2018-10-15 | pcc        | 1       |
    | 2018-10-05 | bite       | 1       |
    | 2018-09-21 | bite       | 4       |
    | 2018-09-18 | bite       | 2       |
    | 2018-09-18 | bite       | 4       |
    +------------+------------+---------+
    """
    dates extract_dates(data)
    streak calculate_streak(dates)
    ... streak __ 0


___ test_streak_of_1_day_can_still_make_today
    data """
    +------------+------------+---------+
    | date       | activity   | count   |
    |------------+------------+---------|
    | 2018-11-11 | pcc        | 1       |
    | 2018-11-09 | 100d       | 1       |
    | 2018-11-07 | 100d       | 2       |
    | 2018-10-23 | pcc        | 1       |
    | 2018-10-15 | pcc        | 1       |
    | 2018-10-05 | bite       | 1       |
    | 2018-09-21 | bite       | 4       |
    | 2018-09-18 | bite       | 2       |
    | 2018-09-18 | bite       | 4       |
    +------------+------------+---------+
    """
    dates extract_dates(data)
    streak calculate_streak(dates)
    ... streak __ 1


___ test_streak_of_1_day_thanks_to_todays_progress
    data """
    +------------+------------+---------+
    | date       | activity   | count   |
    |------------+------------+---------|
    | 2018-11-12 | pcc        | 1       |
    | 2018-11-09 | 100d       | 1       |
    | 2018-11-07 | 100d       | 2       |
    | 2018-10-15 | pcc        | 1       |
    | 2018-10-15 | pcc        | 1       |
    | 2018-10-05 | bite       | 1       |
    | 2018-09-21 | bite       | 4       |
    | 2018-09-18 | bite       | 2       |
    | 2018-09-16 | bite       | 4       |
    +------------+------------+---------+
    """
    dates extract_dates(data)
    streak calculate_streak(dates)
    ... streak __ 1


___ test_streak_of_3_days
    data """
    +------------+------------+---------+
    | date       | activity   | count   |
    |------------+------------+---------|
    | 2018-11-12 | pcc        | 1       |
    | 2018-11-11 | 100d       | 1       |
    | 2018-11-10 | 100d       | 2       |
    | 2018-10-15 | pcc        | 1       |
    | 2018-10-15 | pcc        | 1       |
    | 2018-10-05 | bite       | 1       |
    | 2018-09-21 | bite       | 4       |
    | 2018-09-18 | bite       | 2       |
    | 2018-09-16 | bite       | 4       |
    +------------+------------+---------+
    """
    dates extract_dates(data)
    streak calculate_streak(dates)
    ... streak __ 3


___ test_streak_of_10_days
    data """
    +------------+------------+---------+
    | date       | activity   | count   |
    |------------+------------+---------|
    | 2018-11-11 | pcc        | 1       |
    | 2018-11-10 | 100d       | 1       |
    | 2018-11-09 | 100d       | 2       |
    | 2018-11-08 | pcc        | 1       |
    | 2018-11-07 | pcc        | 1       |
    | 2018-11-06 | bite       | 1       |
    | 2018-11-05 | bite       | 4       |
    | 2018-11-04 | bite       | 2       |
    | 2018-11-03 | bite       | 4       |
    | 2018-11-02 | 100d       | 2       |
    +------------+------------+---------+
    """
    dates extract_dates(data)
    streak calculate_streak(dates)
    ... streak __ 10


___ test_streak_of_almost_10_days_but_gap_so_only_5_days
    data """
    +------------+------------+---------+
    | date       | activity   | count   |
    |------------+------------+---------|
    | 2018-11-11 | pcc        | 1       |
    | 2018-11-10 | 100d       | 1       |
    | 2018-11-09 | 100d       | 2       |
    | 2018-11-08 | pcc        | 1       |
    | 2018-11-07 | pcc        | 1       |
    | 2018-11-05 | bite       | 4       |
    | 2018-11-04 | bite       | 2       |
    | 2018-11-03 | bite       | 4       |
    | 2018-11-02 | 100d       | 2       |
    +------------+------------+---------+
    """
    dates extract_dates(data)
    streak calculate_streak(dates)
    ... streak __ 5


___ test_streak_of_5_days_dates_out_of_order
    data """
    +------------+------------+---------+
    | date       | activity   | count   |
    |------------+------------+---------|
    | 2018-11-11 | pcc        | 1       |
    | 2018-11-07 | pcc        | 1       |
    | 2018-11-09 | 100d       | 2       |
    | 2018-11-10 | 100d       | 1       |
    | 2018-11-08 | pcc        | 1       |
    +------------+------------+---------+
    """
    dates extract_dates(data)
    streak calculate_streak(dates)
    ... streak __ 5