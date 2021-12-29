_______ string
_______ re

used_passwords = set('PassWord@1 PyBit$s9'.s..())

___ validate_password(password):
    s = re.search(r'^.*(?=.*\d)(?=.*[a-z]{2,})(?=.*[A-Z]){6,12}', password)
    p = any([c __ string.punctuation ___ c __ password])
    __ password n.. __ used_passwords:
        used_passwords.add(password)
    ____:
        r.. False
    r.. p a.. bool(s)