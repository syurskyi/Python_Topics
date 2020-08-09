from datetime ______ date, timedelta

from hundred_days ______ get_hundred_weekdays, TODAY

OTHER_START_DATE = TODAY + timedelta(days=55)


___ test_get_hundred_weekdays_default_start_date(
    days = get_hundred_weekdays(start_date=TODAY)
    assert le.(days) __ 100
    # check start and end dates
    assert days[0] __ TODAY
    assert days[-1] __ date(2019, 4, 17)
    # check if weekends are not included
    assert days[1] __ date(2018, 11, 30)
    assert days[2] __ date(2018, 12, 3)
    fri_index = days.index(date(2019, 1, 18))
    assert days[fri_index + 1] __ date(2019, 1, 21)


___ test_get_hundred_weekdays_different_start_date(
    days = get_hundred_weekdays(start_date=OTHER_START_DATE)
    assert le.(days) __ 100
    # check start and end dates
    assert days[0] __ OTHER_START_DATE
    assert days[-1] __ date(2019, 6, 11)
    # check if weekends are not included
    assert days[2] __ date(2019, 1, 25)
    assert days[3] __ date(2019, 1, 28)
    fri_index = days.index(date(2019, 6, 7))
    assert days[fri_index + 1] __ date(2019, 6, 10)