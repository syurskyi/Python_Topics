import re


class Mind:

    def __init__(self):
        pass

    def think(self, query):
        if 'sum' in query:  # Check if string 'sum' is in query
            numbers = re.findall(r'\b\d+\b', query)  # Extract the numbers. E.g. ['1', '2']
            numbers = [float(item) for item in numbers]  # Convert the numbers into floats [1.0, 2.0]
            return sum(numbers)  # Return the sum of the numbers


class Robot:

    def __init__(self):
        self.mind = Mind()  # When Robot is initialized with Robot(), that will also initialize Mind

    def print_out(self, query):
        self.mind = Mind()  # When Robot is initialized with Robot(), that will also initialize Mind
        print(self.mind.think(query))  # Prints out the output returned by mind.think(query)

    def write_down(self, query):
        self.mind = Mind()  # When Robot is initialized with Robot(), that will also initialize Mind

        with open("new.txt", "w") as file:
            file.write(str(self.mind.think(query)))
