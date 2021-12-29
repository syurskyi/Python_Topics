import re


___ validate_license(key: str) -> bool:
    """Write a regex that matches a PyBites license key
       (e.g. PB-U8N435EH-PG65PW87-IXPWQG5T-898XSZI4)
    """
    key_end = ''.join(key.split('-')[1:])
    start = bool(re.match(r'^PB', key))
    split_count = [bool(x) for x in [len(entry)  == 8 for entry in key_end]]
    character_check = bool(re.match('^[a-zA-Z0-9]+$', key_end))
    return start and split_count and character_check