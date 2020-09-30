import re

class Robot:

    def __init__(self):
        pass

    def speak(self, query):
        if 'sum' in query:
            numbers = re.findall(r'\b\d+\b', query)
            numbers = [float(item) for item in numbers]
            return sum(numbers)