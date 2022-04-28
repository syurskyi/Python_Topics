c_ RecordScore
    """Class to track a game's maximum score"""

    ___ -
        high_score f__ '-inf'

    ___ -c  score
        score score
        __ score > high_score:
            high_score score
        r.. high_score


record ?

print( ?-6
print( ?-4
print( ?-2
print( ?-3