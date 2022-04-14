_______ p__

____ ? _______ ?


?p__.f..()
___ record
    """Make a RecordScore object with a few scores"""
    record ?
     ? 10)
     ? 9)
     ? 11)  # initial max
     ? 5)
    r.. ?


___ test_record_unbeaten(record
    ...  ? 9) __ 11
     ? 10)
     ? 2)
    ...  ? 4) __ 11


___ test_record_got_beaten record
    ...  ? 4) __ 11
     ? 3)
     ? 12)  # new max
    ...  ? 4) __ 12
     ? 5)
     ? 16)  # new max
    ...  ? 4) __ 16


___ test_record_got_beaten_negative_values
    record ?
     ? -5)
    ...  ? -4) __ -4
    ...  ? -6) __ -4
    ...  ? -2) __ -2