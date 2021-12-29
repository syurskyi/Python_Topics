_______ string
_______ re

used_passwords = set('PassWord@1 PyBit$s9'.split())

___ validate_password(password):
    c = re.compile(
        r'^.*(?=.*\d)(?=.*[a-z]{2,})(?=.*[A-Z])[\w\d]{6,12}$')
    s = re.search(c, password)
    p = any([c __ string.punctuation ___ c __ password])
    __ password n.. __ used_passwords:
        used_passwords.add(password)
    r.. p and bool(s)