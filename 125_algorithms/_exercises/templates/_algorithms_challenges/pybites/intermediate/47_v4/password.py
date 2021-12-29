import string
import re

PUNCTUATION_CHARS = list(string.punctuation)

used_passwords = set('PassWord@1 PyBit$s9'.split())

"""
is between 6 and 12 chars long (both inclusive)
has at least 1 digit [0-9]
has at least two lowercase chars [a-z]
has at least one uppercase char [A-Z]
has at least one punctuation char (use: PUNCTUATION_CHARS)
Has not been used before (use: used_passwords)
"""


___ validate_password(password):

    length = 6 <= len(password) <= 12
    digit = len(re.findall(r'[0-9]', password)) >= 1
    lower = len(re.findall(r'[a-z]', password)) >= 1
    upper = len(re.findall(r'[A-Z]', password)) >= 1
    punc = any([c in PUNCTUATION_CHARS for c in password])
    new = password not in used_passwords

    valid = length and digit and lower and upper and punc and new

    __ valid:
        used_passwords.add(password)

    return valid
