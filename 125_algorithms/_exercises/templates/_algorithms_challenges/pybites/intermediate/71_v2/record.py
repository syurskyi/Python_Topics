class RecordScore():
    """Class to track a game's maximum score"""

    ___ __init__(self):
        self.max_score = float("-inf")


    ___ __call__(self,score):
        self.max_score = max(self.max_score,score)
        r.. self.max_score
