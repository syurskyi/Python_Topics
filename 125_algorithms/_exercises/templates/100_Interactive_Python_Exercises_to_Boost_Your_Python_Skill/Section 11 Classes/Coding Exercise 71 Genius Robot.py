import re

class Robot:

    ___ __init__(self):
        pass

    ___ speak(self, query):
        if 'sum' __ query:
            numbers = re.findall(r'\b\d+\b', query)
            numbers = [float(item) ___ item __ numbers]
            r_ sum(numbers)