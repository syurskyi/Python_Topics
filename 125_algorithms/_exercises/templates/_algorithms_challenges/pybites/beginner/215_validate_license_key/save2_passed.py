_______ __


___ validate_license(key: s..) __ bool:
    """Write a regex that matches a PyBites license key
       (e.g. PB-U8N435EH-PG65PW87-IXPWQG5T-898XSZI4)
    """
    start = bool(__.m..(r'^PB', key))
    split_count = a..(bool(x) 
                      ___ x __ [l..(entry)  __ 8
                                ___ entry __ key.s..('-')[1:]])
    character_check = bool(
        __.m..('^[a-zA-Z0-9]+$', ''.j..(key.s..('-')[1:])))
    r.. start a.. split_count a.. character_check