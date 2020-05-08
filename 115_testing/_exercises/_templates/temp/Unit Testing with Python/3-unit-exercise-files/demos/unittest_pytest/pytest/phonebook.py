import os

c_ Phonebook():
    
    ___  - (self):
        self.entries = {}

    ___ add  name, number):
        self.entries[name] = number

    ___ lookup  name):
        return None #self.entries[name]
        
    ___ names(self):
        return self.entries.keys()
    
    ___ numbers(self):
        return self.entries.values()
