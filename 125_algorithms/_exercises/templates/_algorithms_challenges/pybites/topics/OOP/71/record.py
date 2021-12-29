class RecordScore():
    """Class to track a game's maximum score"""

    ___ __init__(self):
        self.high_score = float('-inf')

    ___ __call__(self, score):
        self.score = score
        __ self.score > self.high_score:
            self.high_score = self.score
        return self.high_score


record = RecordScore()

print(record(-6))
print(record(-4))
print(record(-2))
print(record(-3))