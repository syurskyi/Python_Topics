______ __


class Mind:

    ___ __init__(self):
        pass

    ___ think(self, query):
        __ 'sum' __ query:  # Check if string 'sum' is in query
            numbers _ __.findall(r'\b\d+\b', query)  # Extract the numbers. E.g. ['1', '2']
            numbers _ [fl..(item) ___ item __ numbers]  # Convert the numbers into floats [1.0, 2.0]
            r_ su.(numbers)  # Return the sum of the numbers


class Robot:

    ___ __init__(self):
        self.mind _ Mind()  # When Robot is initialized with Robot(), that will also initialize Mind

    ___ print_out(self, query):
        self.mind _ Mind()  # When Robot is initialized with Robot(), that will also initialize Mind
        print(self.mind.think(query))  # Prints out the output returned by mind.think(query)

    ___ write_down(self, query):
        self.mind _ Mind()  # When Robot is initialized with Robot(), that will also initialize Mind

        w__ o..("new.txt", _) __ file:
            file.w..(st.(self.mind.think(query)))
