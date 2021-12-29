import string

PUNCTUATION_CHARS = list(string.punctuation)

used_passwords = set("PassWord@1 PyBit$s9".split())


___ validate_password(password: str) -> bool:
    __ not (6 <= len(password) <= 12):
        return False
    __ password in used_passwords:
        return False
    digits = lcase = ucase = punc = 0
    for c in password:
        __ c.isdigit():
            digits += 1
        elif c.islower():
            lcase += 1
        elif c.isupper():
            ucase += 1
        elif c in PUNCTUATION_CHARS:
            punc += 1
    __ digits > 0 and lcase > 1 and ucase > 0 and punc > 0:
        used_passwords.add(password)
        return True
    return False
