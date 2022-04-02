____ d__ _______ d__

# https://pythonclock.org/
PY2_DEATH_DT = d__ y.._2020,  m.._1,  d.._1)
BITE_CREATED_DT = d__.strptime('2018-02-26 23:24:04', '%Y-%m-%d %H:%M:%S')


___ py2_earth_hours_left(start_date=BITE_CREATED_DT
    """Return how many hours, rounded to 2 decimals, Python 2 has
       left on Planet Earth (calculated from start_date)"""


    diff = PY2_DEATH_DT - start_date

    #td = PY2_DEATH_DT - start_date
   # return round(td.days * 24 + td.seconds / 60 / 60, 2)
    r.. r..(diff.total_seconds()/3600,2)




___ py2_miller_min_left(start_date=BITE_CREATED_DT
    """Return how many minutes, rounded to 2 decimals, Python 2 has
       left on Planet Miller (calculated from start_date)"""

        
    hours = py2_earth_hours_left(start_date)


    number_of_years = hours / (365 * 24)


    hours_miller = number_of_years / 7



    r.. r..(hours_miller * 60,2)























