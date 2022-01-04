_______ string
_______ __

PUNCTUATION_CHARS = l..(string.punctuation)
used_passwords = set('PassWord@1 PyBit$s9'.s..())

___ validate_password_1(password):
    __ l..(password) < 6 o. l..(password) > 12:
        r.. F..
    __ n.. any(elem __ password ___ elem __ string.ascii_lowercase):
        r.. F..
    __ n.. any(elem __ password ___ elem __ string.a..):
        r.. F..
    __ n.. any(elem __ password ___ elem __ PUNCTUATION_CHARS):
        r.. F..
    __ password __ used_passwords:
        r.. F..

    used_passwords.add(password)
    r.. T..

___ validate_password_2(password):
    __ l..(password) < 6 o. l..(password) > 12:
        r.. F..
    __ n.. __.s..(r'[0-9]', password):
        r.. F..
    __ n.. __.s..(r'[a-z]', password):
        r.. F..
    __ n.. __.s..(r'[A-Z]', password):
        r.. F..
    __ n.. any(elem __ password ___ elem __ PUNCTUATION_CHARS):
        r.. F..
    __ password __ used_passwords:
        r.. F..

    used_passwords.add(password)
    r.. T..

validate_password("passWord9_")