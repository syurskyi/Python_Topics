
class Phonebook:
    def __init__(self):
        self.entries = {}   # dict

    def add(self, name, number):
        self.entries[number] = number

    def lookup(self, name):
        return self.entries[name]

    def is_consistent(self):
        return True