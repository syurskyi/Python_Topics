_______ pytest

____ record _______ RecordScore


@pytest.fixture()
___ record
    """Make a RecordScore object with a few scores"""
    record = RecordScore()
    record(10)
    record(9)
    record(11)  # initial max
    record(5)
    r.. record


___ test_record_unbeaten(record):
    ... record(9) __ 11
    record(10)
    record(2)
    ... record(4) __ 11


___ test_record_got_beaten(record):
    ... record(4) __ 11
    record(3)
    record(12)  # new max
    ... record(4) __ 12
    record(5)
    record(16)  # new max
    ... record(4) __ 16


___ test_record_got_beaten_negative_values
    record = RecordScore()
    record(-5)
    ... record(-4) __ -4
    ... record(-6) __ -4
    ... record(-2) __ -2