"""
Complete the validate_license function writing a regular expression that matches a PyBites
license key which:

Starts with PB,
following 4 times dash (-) and 8 chars which can be upper case chars or digits,
for example: PB-U8N435EH-PG65PW87-IXPWQG5T-898XSZI4 would be a valid license key.
Return a bool (we added some type hinting for convenience).

Example how this function would work:

>>> import re
>>> from license import validate_license
>>> validate_license('PB-U8N435EH-PG65PW87-IXPWQG5T-898XSZI4')
True
>>> validate_license('pb-U8N435EH-PG65PW87-IXPWQG5T-898XSZI4')
False
>>> validate_license('bogus')
False
>>> validate_license('PB-U8N435EH-PG65PW87-IXPWQG5T-898XSZ..')
False
"""

"""
Bite attempted/solved on 22.03.2020

It was fairly easy, I only had to review regexp syntax here:
https://www.debuggex.com/cheatsheet/regex/python
"""

import re


def validate_license(key: str) -> bool:
    """Write a regex that matches a PyBites license key
       (e.g. PB-U8N435EH-PG65PW87-IXPWQG5T-898XSZI4)
    """
    if(re.match(r"^PB-(\d|\w){8}-(\d|\w){8}-(\d|\w){8}-(\d|\w){8}$", key)):
        return True
    else:
        return False

print(validate_license("PB-U8N435EH-PG65PW87-IXPWQG5T-898XSZI4"))
print(validate_license("vogus"))

