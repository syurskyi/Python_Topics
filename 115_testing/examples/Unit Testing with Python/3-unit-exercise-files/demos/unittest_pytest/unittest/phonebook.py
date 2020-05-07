import os

class Phonebook():
    
    def __init__(self):
        self.entries = {}

    def add(self, name, number):
        self.entries[name] = number

    def lookup(self, name):
        return None #self.entries[name]
        
    def names(self):
        return self.entries.keys()
    
    def numbers(self):
        return self.entries.values()
