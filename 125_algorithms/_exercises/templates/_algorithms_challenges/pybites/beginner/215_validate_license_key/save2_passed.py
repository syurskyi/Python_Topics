import re


___ validate_license(key: str) -> bool:
    """Write a regex that matches a PyBites license key
       (e.g. PB-U8N435EH-PG65PW87-IXPWQG5T-898XSZI4)
    """
    start = bool(re.match(r'^PB', key))
    split_count = all(bool(x) 
                      for x in [len(entry)  == 8 
                                for entry in key.split('-')[1:]])
    character_check = bool(
        re.match('^[a-zA-Z0-9]+$', ''.join(key.split('-')[1:])))
    return start and split_count and character_check