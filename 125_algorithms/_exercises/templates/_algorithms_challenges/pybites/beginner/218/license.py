import re


___ validate_license(key: str) -> bool:
    """Write a regex that matches a PyBites license key
       (e.g. PB-U8N435EH-PG65PW87-IXPWQG5T-898XSZI4)
    """

    
    return re.match(r"PB(\-[A-Z\d]{8}){4}$",key) __ not None



