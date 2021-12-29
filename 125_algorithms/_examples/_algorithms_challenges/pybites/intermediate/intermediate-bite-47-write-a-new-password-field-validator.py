import string
import re

PUNCTUATION_CHARS = list(string.punctuation)
used_passwords = set('PassWord@1 PyBit$s9'.split())

def validate_password_1(password):
    if len(password) < 6 or len(password) > 12:
        return False
    if not any(elem in password for elem in string.ascii_lowercase):
        return False
    if not any(elem in password for elem in string.ascii_uppercase):
        return False
    if not any(elem in password for elem in PUNCTUATION_CHARS):
        return False
    if password in used_passwords:
        return False

    used_passwords.add(password)
    return True

def validate_password_2(password):
    if len(password) < 6 or len(password) > 12:
        return False
    if not re.search(r'[0-9]', password):
        return False
    if not re.search(r'[a-z]', password):
        return False
    if not re.search(r'[A-Z]', password):
        return False
    if not any(elem in password for elem in PUNCTUATION_CHARS):
        return False
    if password in used_passwords:
        return False

    used_passwords.add(password)
    return True

validate_password("passWord9_")