import string
import re

used_passwords = set('PassWord@1 PyBit$s9'.split())

def validate_password(password):
    c = re.compile(
        r'^.*(?=.*\d)(?=.*[a-z]{2,})(?=.*[A-Z])[\w\d]{6,12}$')
    s = re.search(c, password)
    p = any([c in string.punctuation for c in password])
    if password not in used_passwords:
        used_passwords.add(password)
    return p and bool(s)