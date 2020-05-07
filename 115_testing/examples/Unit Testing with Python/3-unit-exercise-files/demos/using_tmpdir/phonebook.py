import os

class Phonebook():
    
    def __init__(self, cachedir):
        self.entries = {}
        self.filename = "phonebook.txt"
        self.file_cache = open(os.path.join(str(cachedir), self.filename), "w")

    def add(self, name, number):
        self.entries[name] = number

    def lookup(self, name):
        return self.entries[name]
        
    def names(self):
        return self.entries.keys()
    
    def numbers(self):
        return self.entries.values()
        
    def clear(self):
        self.entries = {}
        self.file_cache.close()
        os.remove(self.filename)

