____ d__ _______ d__

# https://pythonclock.org/
PY2_DEATH_DT = d__ y.._2020,  m.._1,  d.._1)
BITE_CREATED_DT = d__.s..('2018-02-26 23:24:04', '%Y-%m-%d %H:%M:%S')


___ py2_earth_hours_left(start_date=BITE_CREATED_DT
    """Return how many hours, rounded to 2 decimals, Python 2 has
       left on Planet Earth (calculated from start_date)"""
    t__ = a..(start_date - PY2_DEATH_DT)
    days, seconds = t__.days, t__.seconds
    r.. r..((days * 24) + (seconds / 3600), 2)


___ py2_miller_min_left(start_date=BITE_CREATED_DT
    """Return how many minutes, rounded to 2 decimals, Python 2 has
       left on Planet Miller (calculated from start_date)"""
    earth_hours = py2_earth_hours_left(start_date)
    earth_years = earth_hours / 8760
    miller_hours = earth_years / 7
    r.. r..(miller_hours * 60, 2)