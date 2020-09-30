______ re

class Robot:

    ___ __init__(self):
        pass

    ___ speak(self, query):
        __ 'sum' __ query:
            numbers _ re.findall(r'\b\d+\b', query)
            numbers _ [float(item) ___ item __ numbers]
            r_ su.(numbers)