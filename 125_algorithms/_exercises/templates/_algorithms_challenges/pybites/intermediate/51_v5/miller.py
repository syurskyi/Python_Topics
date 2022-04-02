____ d__ _______ d__

# https://pythonclock.org/
PY2_DEATH_DT = d__ y.._2020,  m.._1,  d.._1)
BITE_CREATED_DT = d__.strptime('2018-02-26 23:24:04', '%Y-%m-%d %H:%M:%S')

SEC_PER_HOUR = 60 * 60
SEC_PER_DAY = SEC_PER_HOUR * 24
SEC_PER_YEAR = SEC_PER_DAY * 365
SEC_PER_HOUR_MILLER = SEC_PER_YEAR * 7
SEC_PER_MINUTE_MILLER = SEC_PER_HOUR_MILLER / 60


___ py2_earth_hours_left(start_date=BITE_CREATED_DT
    """Return how many hours, rounded to 2 decimals, Python 2 has
       left on Planet Earth (calculated from start_date)"""
    r.. r..((PY2_DEATH_DT - start_date).total_seconds() / SEC_PER_HOUR, 2)


___ py2_miller_min_left(start_date=BITE_CREATED_DT
    """Return how many minutes, rounded to 2 decimals, Python 2 has
       left on Planet Miller (calculated from start_date)"""
    r.. r..((PY2_DEATH_DT - start_date).total_seconds() / SEC_PER_MINUTE_MILLER, 2)
