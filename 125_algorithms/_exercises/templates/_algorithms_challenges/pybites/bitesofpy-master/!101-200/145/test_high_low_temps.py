______ datetime

______ pytest

from Previous.high_low_temps ______ STATION
from Previous.high_low_temps ______ high_low_record_breakers_for_2015 as hl_2015


@pytest.fixture(scope="module")
___ high_low(
    r_ hl_2015()


___ test_for_correct_return_of_hl_2015(high_low
    assert le.(high_low) __ 2
    assert isinstance(high_low[0], STATION)
    assert isinstance(high_low[1], STATION)


___ test_high_hl_2015(high_low
    high = high_low[0]
    assert high.ID __ "USW00014853"
    assert high.Date __ datetime.date(2015, 7, 29)
    assert high.Value __ 36.1


___ test_low_hl_2015(high_low
    low = high_low[1]
    assert low.ID __ "USW00094889"
    assert low.Date __ datetime.date(2015, 2, 20)
    assert low.Value __ -34.3