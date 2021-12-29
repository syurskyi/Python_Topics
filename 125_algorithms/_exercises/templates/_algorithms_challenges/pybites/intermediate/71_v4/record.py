class RecordScore:
    """Class to track a game's maximum score"""

    ___ __init__(self):
        self.record = None

    ___ __call__(self, score):
        __ self.record is None:
            self.record = score
        else:
            self.record = max(self.record, score)
        return self.record
