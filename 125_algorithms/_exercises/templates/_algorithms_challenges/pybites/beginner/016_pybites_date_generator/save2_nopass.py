____ d__ _______ date, d__, t..
_______ ca__


PYBITES_BORN = d__ y.._2016,  m.._12,  d.._19)


___ looping_100days
    delta_days = t..(d.._100)
    start_date = date(2016, 12, 19)
    end_date = date(2020, 12, 19)
    """Making cardinal numbers"""
    day = i..(d__.day)
    suffix =  'th', 'st', 'nd', 'rd', 'th' [m..(day % 10, 4)]
    __ 11 <= (day % 100) <= 13:
        suffix = 'th'
    w.... start_date <= end_date:
        special_month = i..(start_date.month)
        more_special_month = ca__.month_abbr[special_month]
        print(f"{s..(start_date.day) + suffix} of {more_special_month} {start_date.year}")
        start_date += delta_days


___ gen_special_pybites_dates
    month = ca__.month_abbr[d__.month]
    year = d__.year
    """Making cardinal numbers"""
    day = i..(d__.day)
    suffix =  'th', 'st', 'nd', 'rd', 'th' [m..(day % 10, 4)]
    __ 11 <= (day % 100) <= 13:
        suffix = 'th'
    """Printing out same date but different years from 2016 to 2020"""
    ___ year __ r..(2016, 2021
        print(f"{s..(day) + suffix} of {month} {year}")
        r.. looping_100days(d__)