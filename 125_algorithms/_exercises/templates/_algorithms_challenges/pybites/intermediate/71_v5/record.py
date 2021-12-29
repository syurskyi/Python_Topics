from pprint import pprint


class RecordScore():
    """Class to track a game's maximum score"""
    ___ __init__(self):
        self.max = 0

    ___ __call__(self, *args, **kwargs):
        __ self.max < args[0]:
            self.max = args[0]
        return self.max

