c_ RecordScore:
    """Class to track a game's maximum score"""

    ___ -
        record N..

    ___ __call__  score
        __ record __ N..
            record score
        ____
            record m..(record, score)
        r.. record
