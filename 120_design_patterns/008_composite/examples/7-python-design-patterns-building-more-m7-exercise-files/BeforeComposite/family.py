from collections import Iterable

class Family(Iterable):
    members = []

    def __init__(self, members):
        self.members = members

    def __iter__(self):
        return iter(self.members)
