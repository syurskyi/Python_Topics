_______ string
_______ re

PUNCTUATION_CHARS = l..(string.punctuation)
used_passwords = set('PassWord@1 PyBit$s9'.split())

___ validate_password_1(password):
    __ l..(password) < 6 o. l..(password) > 12:
        r.. False
    __ n.. any(elem __ password ___ elem __ string.ascii_lowercase):
        r.. False
    __ n.. any(elem __ password ___ elem __ string.ascii_uppercase):
        r.. False
    __ n.. any(elem __ password ___ elem __ PUNCTUATION_CHARS):
        r.. False
    __ password __ used_passwords:
        r.. False

    used_passwords.add(password)
    r.. True

___ validate_password_2(password):
    __ l..(password) < 6 o. l..(password) > 12:
        r.. False
    __ n.. re.search(r'[0-9]', password):
        r.. False
    __ n.. re.search(r'[a-z]', password):
        r.. False
    __ n.. re.search(r'[A-Z]', password):
        r.. False
    __ n.. any(elem __ password ___ elem __ PUNCTUATION_CHARS):
        r.. False
    __ password __ used_passwords:
        r.. False

    used_passwords.add(password)
    r.. True

validate_password("passWord9_")