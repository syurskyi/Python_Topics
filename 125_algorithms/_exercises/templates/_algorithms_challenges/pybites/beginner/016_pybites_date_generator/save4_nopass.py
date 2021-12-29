____ datetime _______ date, datetime, timedelta
_______ calendar


PYBITES_BORN = datetime(year=2016, month=12, day=19)


___ looping_100days(datetime):
    delta_days = timedelta(days=100)
    start_date = date(2016, 12, 19)
    end_date = date(2020, 12, 19)
    """Making cardinal numbers"""
    day = int(datetime.day)
    suffix = ['th', 'st', 'nd', 'rd', 'th'][m..(day % 10, 4)]
    __ 11 <= (day % 100) <= 13:
        suffix = 'th'
    while start_date <= end_date:
        special_month = int(start_date.month)
        more_special_month = calendar.month_abbr[special_month]
        print(f"{str(start_date.day) + suffix} of {more_special_month} {start_date.year}")
        start_date += delta_days


___ gen_special_pybites_dates(datetime):
    month = calendar.month_abbr[datetime.month]
    year = datetime.year
    """Making cardinal numbers"""
    day = int(datetime.day)
    suffix = ['th', 'st', 'nd', 'rd', 'th'][m..(day % 10, 4)]
    __ 11 <= (day % 100) <= 13:
        suffix = 'th'
    """Printing out same date but different years from 2016 to 2020"""
    ___ year __ r..(2016, 2021):
        print(f"{str(day) + suffix} of {month} {year}")
    r.. looping_100days(datetime)