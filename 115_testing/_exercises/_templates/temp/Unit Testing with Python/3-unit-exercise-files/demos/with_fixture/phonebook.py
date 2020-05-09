______ os

c_ Phonebook():
    
    ___  - 
        entries _ {}
        filename _ "phonebook.txt"
        file_cache _ open(filename, "w")

    ___ add  name, number):
        entries[name] _ number

    ___ lookup  name):
        r_ entries[name]
        
    ___ names
        r_ entries.keys()
    
    ___ numbers
        r_ entries.values()
        
    ___ clear
        entries _ {}
        file_cache.close()
        os.remove(filename)

