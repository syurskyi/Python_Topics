class RecordScore:
    """Class to track a game's maximum score"""

    def __init__(self):
        self.record = None

    def __call__(self, score):
        if self.record is None:
            self.record = score
        else:
            self.record = max(self.record, score)
        return self.record
