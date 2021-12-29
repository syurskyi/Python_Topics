import string
import re

PUNCTUATION_CHARS = list(string.punctuation)

used_passwords = set('PassWord@1 PyBit$s9'.split())


def validate_password(password):
    c = re.compile(
        r'^(?=.*\d)(?=.*[a-z]{2,})(?=.*[A-Z])(?=.*[PUNCTUATION_CHARS])[\w\dPUNCTUATION_CHARS]{6,12}$')
    s = re.search(c, password)
    if password not in used_passwords and bool(s):
        used_passwords.add(password)
        return bool(s)
    else:
        return False