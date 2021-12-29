import string
import re

used_passwords = set('PassWord@1 PyBit$s9'.split())

def validate_password(password):
    s = re.search(r'^.*(?=.*\d)(?=.*[a-z]{2,})(?=.*[A-Z]){6,12}', password)
    p = any([c in string.punctuation for c in password])
    if password not in used_passwords:
        used_passwords.add(password)
    else:
        return False
    return p and bool(s)