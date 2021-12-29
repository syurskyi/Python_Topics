import string
import re

PUNCTUATION_CHARS = list(string.punctuation)

used_passwords = set('PassWord@1 PyBit$s9'.split())


def validate_password(password):
    c = re.compile(
        r'^.*(?=.*\d)(?=.*[a-z]{2,})(?=.*[A-Z])[\w\d]{6,12}$')
    s = re.search(c, password)
    if (password not in used_passwords) and (bool(s) == True):
        for c in password:
            if c in PUNCTUATION_CHARS:
                used_passwords.add(password)
                return bool(s)
    else:
        return False