c_ RecordScore():
    """Class to track a game's maximum score"""

    ___ - ):
        high_score = float('-inf')

    ___ __call__(self, score):
        score = score
        __ score > high_score:
            high_score = score
        r.. high_score


record = RecordScore()

print(record(-6))
print(record(-4))
print(record(-2))
print(record(-3))