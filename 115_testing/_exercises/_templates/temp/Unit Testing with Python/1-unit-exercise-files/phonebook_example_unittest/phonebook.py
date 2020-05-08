
c_ Phonebook:
    ___  - (self):
        self.entries = {}
    
    ___ add  name, number):
        self.entries[name] = number
    
    ___ lookup  name):
        return self.entries[name]
        
    ___ is_consistent(self):
        return True