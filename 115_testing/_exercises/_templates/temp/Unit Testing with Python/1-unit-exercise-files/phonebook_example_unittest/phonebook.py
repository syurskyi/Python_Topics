
c_ Phonebook:
    ___  -
        entries _ {}
    
    ___ add  name, number):
        entries[name] _ number
    
    ___ lookup  name):
        r_ entries[name]
        
    ___ is_consistent
        r_ True