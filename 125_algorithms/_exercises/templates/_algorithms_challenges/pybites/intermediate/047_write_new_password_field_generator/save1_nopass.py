_______ string
_______ re

PUNCTUATION_CHARS = l..(string.punctuation)

used_passwords = set('PassWord@1 PyBit$s9'.split())


___ validate_password(password):
    c = re.compile(
        r'^(?=.*\d)(?=.*[a-z]{2,})(?=.*[A-Z])(?=.*[PUNCTUATION_CHARS]){6,12}')
    s = re.search(c, password)
    __ password n.. __ used_passwords and bool(s):
        used_passwords.add(password)
        r.. bool(s)
    ____:
        r.. n.. True