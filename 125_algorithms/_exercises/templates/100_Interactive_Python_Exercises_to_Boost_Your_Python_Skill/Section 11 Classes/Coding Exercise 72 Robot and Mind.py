import re


class Mind:

    ___ __init__(self):
        pass

    ___ think(self, query):
        if 'sum' __ query:  # Check if string 'sum' is in query
            numbers = re.findall(r'\b\d+\b', query)  # Extract the numbers. E.g. ['1', '2']
            numbers = [float(item) ___ item __ numbers]  # Convert the numbers into floats [1.0, 2.0]
            r_ sum(numbers)  # Return the sum of the numbers


class Robot:

    ___ __init__(self):
        self.mind = Mind()  # When Robot is initialized with Robot(), that will also initialize Mind

    ___ print_out(self, query):
        self.mind = Mind()  # When Robot is initialized with Robot(), that will also initialize Mind
        print(self.mind.think(query))  # Prints out the output returned by mind.think(query)

    ___ write_down(self, query):
        self.mind = Mind()  # When Robot is initialized with Robot(), that will also initialize Mind

        with open("new.txt", "w") as file:
            file.write(str(self.mind.think(query)))
