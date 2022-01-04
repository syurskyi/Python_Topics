_______ d__

_______ pytest

____ high_low_temps _______ STATION
____ high_low_temps _______ high_low_record_breakers_for_2015 __ hl_2015


@pytest.fixture(scope="module")
___ high_low
    r.. hl_2015()


___ test_for_correct_return_of_hl_2015(high_low):
    ... l..(high_low) __ 2
    ... isi..(high_low[0], STATION)
    ... isi..(high_low[1], STATION)


___ test_high_hl_2015(high_low):
    high = high_low[0]
    ... high.ID __ "USW00014853"
    ... high.Date __ d__.date(2015, 7, 29)
    ... high.Value __ 36.1


___ test_low_hl_2015(high_low):
    low = high_low[1]
    ... low.ID __ "USW00094889"
    ... low.Date __ d__.date(2015, 2, 20)
    ... low.Value __ -34.3
