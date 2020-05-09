______ os

c_ Phonebook(
    
    ___  -
        entries _ {}

    ___ add  name, number
        entries[name] _ number

    ___ lookup  name
        r_ "foo"#self.entries[name]
        
    ___ names
        r_ entries.keys()
    
    ___ numbers
        r_ entries.values()
        
