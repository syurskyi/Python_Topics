class RecordScore():
    """Class to track a game's maximum score"""
    def __init__(self):
        self.max = None

    def __call__(self, new):
        if self.max == None:
            self.max = new
        else:
            if new > self.max:
                self.max = new
        return self.max