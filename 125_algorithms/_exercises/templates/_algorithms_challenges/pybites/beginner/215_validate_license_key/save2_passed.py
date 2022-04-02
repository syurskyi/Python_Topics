_______ __


___ validate_license(key: s..) __ b..:
    """Write a regex that matches a PyBites license key
       (e.g. PB-U8N435EH-PG65PW87-IXPWQG5T-898XSZI4)
    """
    start = b..(__.m..(r'^PB', key))
    split_count = a..(b..(x) 
                      ___ x __ [l..(entry)  __ 8
                                ___ entry __ key.s..('-')[1:]])
    character_check = b..(
        __.m..('^[a-zA-Z0-9]+$', ''.j..(key.s..('-')[1:])))
    r.. start a.. split_count a.. character_check