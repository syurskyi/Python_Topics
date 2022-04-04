____ d__ _______ date, t..

____ hundred_days _______ get_hundred_weekdays, TODAY

OTHER_START_DATE = TODAY + t..(d.._55)


___ test_get_hundred_weekdays_default_start_date
    days = get_hundred_weekdays(start_date=TODAY)
    ... l..(days) __ 100
    # check start and end dates
    ... days[0] __ TODAY
    ... days[-1] __ date(2019, 4, 17)
    # check if weekends are not included
    ... days[1] __ date(2018, 11, 30)
    ... days[2] __ date(2018, 12, 3)
    fri_index = days.i.. date(2019, 1, 18
    ... days[fri_index + 1] __ date(2019, 1, 21)


___ test_get_hundred_weekdays_different_start_date
    days = get_hundred_weekdays(start_date=OTHER_START_DATE)
    ... l..(days) __ 100
    # check start and end dates
    ... days[0] __ OTHER_START_DATE
    ... days[-1] __ date(2019, 6, 11)
    # check if weekends are not included
    ... days[2] __ date(2019, 1, 25)
    ... days[3] __ date(2019, 1, 28)
    fri_index = days.i.. date(2019, 6, 7
    ... days[fri_index + 1] __ date(2019, 6, 10)
