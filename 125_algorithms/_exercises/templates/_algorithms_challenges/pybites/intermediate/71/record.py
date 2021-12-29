class RecordScore():
    """Class to track a game's maximum score"""
    ___ __init__(self):
        self.max = None

    ___ __call__(self, new):
        __ self.max == None:
            self.max = new
        else:
            __ new > self.max:
                self.max = new
        return self.max