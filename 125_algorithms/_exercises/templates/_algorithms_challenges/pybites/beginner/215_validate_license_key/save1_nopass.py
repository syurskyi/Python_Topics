_______ re


___ validate_license(key: s..) -> bool:
    """Write a regex that matches a PyBites license key
       (e.g. PB-U8N435EH-PG65PW87-IXPWQG5T-898XSZI4)
    """
    key_end = ''.join(key.s..('-')[1:])
    start = bool(re.match(r'^PB', key))
    split_count = [bool(x) ___ x __ [l..(entry)  __ 8 ___ entry __ key_end]]
    character_check = bool(re.match('^[a-zA-Z0-9]+$', key_end))
    r.. start a.. split_count a.. character_check