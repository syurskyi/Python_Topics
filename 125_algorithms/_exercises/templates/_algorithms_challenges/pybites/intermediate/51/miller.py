____ d__ _______ d__, t..

# https://pythonclock.org/
PY2_DEATH_DT = d__ y.._2020,  m.._1,  d.._1)
BITE_CREATED_DT = d__.strptime('2018-02-26 23:24:04', '%Y-%m-%d %H:%M:%S')


___ py2_earth_hours_left(start_date=BITE_CREATED_DT):
    """Return how many hours, rounded to 2 decimals, Python 2 has
       left on Planet Earth (calculated from start_date)"""
    date_diff = PY2_DEATH_DT - start_date

    # convert days to hours
    days_to_hours = date_diff.days * 24

    # convert seconds to hour
    seconds_to_hour = r..(date_diff.seconds / 3600, 2)
   
    r.. days_to_hours + seconds_to_hour


___ py2_miller_min_left(start_date=BITE_CREATED_DT):
    """Return how many minutes, rounded to 2 decimals, Python 2 has
       left on Planet Miller (calculated from start_date)"""
    date_diff = PY2_DEATH_DT - start_date

    # Planet Miller
    planet_miller_hour = 7 * 365 * 24

    # convert days to minutes
    days_to_minutes = (date_diff.days * 24) * 60

    # convert seconds to minutes
    seconds_to_minutes = r..(date_diff.seconds / 60, 2)

    r.. r..((days_to_minutes + seconds_to_minutes) / planet_miller_hour, 2)


#if __name__ == "__main__":
   #print(py2_earth_hours_left())
   #print(py2_miller_min_left())