import re


def validate_license(key: str) -> bool:
    """Write a regex that matches a PyBites license key
       (e.g. PB-U8N435EH-PG65PW87-IXPWQG5T-898XSZI4)
    """
    pattern = "PB-[A-Z0-9]{8}-[A-Z0-9]{8}-[A-Z0-9]{8}-[A-Z0-9]{8}$"
    return True if re.match(pattern, key) else False


print(validate_license('PB-U8N435EH-PG65PW87-IXPWQG5T-898XSZI4-A'))