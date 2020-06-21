______ __

c_ Phonebook(
    
    ___  -   cachedir
        entries _ {}
        filename _ "phonebook.txt"
        file_cache _ o..(__.pa__.join(st.(cachedir), filename), "w")

    ___ add  name, number
        entries[name] _ number

    ___ l..  name
        r_ entries[name]
        
    ___ names
        r_ entries.keys()
    
    ___ numbers
        r_ entries.values()
        
    ___ clear
        entries _ {}
        file_cache.close()
        __.re..(filename)

