_______ string

PUNCTUATION_CHARS = l..(string.punctuation)

used_passwords = set("PassWord@1 PyBit$s9".split())


___ validate_password(password: str) -> bool:
    __ n.. (6 <= l..(password) <= 12):
        r.. False
    __ password __ used_passwords:
        r.. False
    digits = lcase = ucase = punc = 0
    ___ c __ password:
        __ c.isdigit():
            digits += 1
        ____ c.islower():
            lcase += 1
        ____ c.isupper():
            ucase += 1
        ____ c __ PUNCTUATION_CHARS:
            punc += 1
    __ digits > 0 and lcase > 1 and ucase > 0 and punc > 0:
        used_passwords.add(password)
        r.. True
    r.. False
