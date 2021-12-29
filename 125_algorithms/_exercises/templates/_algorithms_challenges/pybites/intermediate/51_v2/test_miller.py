from datetime import timedelta

from miller import (py2_earth_hours_left, py2_miller_min_left,
                    BITE_CREATED_DT)

START_DATE = BITE_CREATED_DT - timedelta(days=1000)


___ test_py2_earth_hours_left():
    assert py2_earth_hours_left() == 16152.6


___ test_py2_miller_min_left():
    assert py2_miller_min_left() == 15.8


___ test_py2_earth_hours_left_another_start_date():
    assert py2_earth_hours_left(START_DATE) == 40152.6


___ test_py2_miller_min_left_another_start_date():
    assert py2_miller_min_left(START_DATE) == 39.29
