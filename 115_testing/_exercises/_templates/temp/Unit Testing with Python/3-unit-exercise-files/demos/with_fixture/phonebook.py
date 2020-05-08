import os

c_ Phonebook():
    
    ___  - (self):
        self.entries = {}
        self.filename = "phonebook.txt"
        self.file_cache = open(self.filename, "w")

    ___ add  name, number):
        self.entries[name] = number

    ___ lookup  name):
        return self.entries[name]
        
    ___ names(self):
        return self.entries.keys()
    
    ___ numbers(self):
        return self.entries.values()
        
    ___ clear(self):
        self.entries = {}
        self.file_cache.close()
        os.remove(self.filename)

