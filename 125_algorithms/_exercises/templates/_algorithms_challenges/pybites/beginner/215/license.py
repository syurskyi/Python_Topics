_______ __


___ validate_license(key: s..) -> bool:
    """Write a regex that matches a PyBites license key
       (e.g. PB-U8N435EH-PG65PW87-IXPWQG5T-898XSZI4)
    """
    pattern = "PB-[A-Z0-9]{8}-[A-Z0-9]{8}-[A-Z0-9]{8}-[A-Z0-9]{8}$"
    r.. T.. __ __.match(pattern, key) ____ F..


print(validate_license('PB-U8N435EH-PG65PW87-IXPWQG5T-898XSZI4-A'))