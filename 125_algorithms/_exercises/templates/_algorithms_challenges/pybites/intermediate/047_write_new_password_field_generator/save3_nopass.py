_______ string
_______ re

PUNCTUATION_CHARS = l..(string.punctuation)

used_passwords = set('PassWord@1 PyBit$s9'.s..())


___ validate_password(password):
    c = re.compile(
        r'^.*(?=.*\d)(?=.*[a-z]{2,})(?=.*[A-Z])[\w\d]{6,12}$')
    s = re.search(c, password)
    __ (password n.. __ used_passwords) a.. (bool(s) __ True):
        ___ c __ password:
            __ c __ PUNCTUATION_CHARS:
                used_passwords.add(password)
                r.. bool(s)
    ____:
        r.. False