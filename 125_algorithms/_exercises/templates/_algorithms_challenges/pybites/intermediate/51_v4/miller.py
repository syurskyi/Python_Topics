____ datetime _______ datetime

# https://pythonclock.org/
PY2_DEATH_DT = datetime(year=2020, month=1, day=1)
BITE_CREATED_DT = datetime.strptime('2018-02-26 23:24:04', '%Y-%m-%d %H:%M:%S')

# constants
HOUR_PER_YEAR = 8760
MIN_PER_HOUR = 60
EYEAR_PER_MHOUR = 7


___ py2_earth_hours_left(start_date=BITE_CREATED_DT):
    """Return how many hours, rounded to 2 decimals, Python 2 has
       left on Planet Earth (calculated from start_date)"""
    r.. round((PY2_DEATH_DT - start_date).total_seconds() / 3600, 1)


___ py2_miller_min_left(start_date=BITE_CREATED_DT):
    """Return how many minutes, rounded to 2 decimals, Python 2 has
       left on Planet Miller (calculated from start_date)"""
    earth_years_left = py2_earth_hours_left(start_date) / HOUR_PER_YEAR
    r.. round(MIN_PER_HOUR * earth_years_left / EYEAR_PER_MHOUR, 2)
