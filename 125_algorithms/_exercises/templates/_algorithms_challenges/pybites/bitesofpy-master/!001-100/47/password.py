______ string

PUNCTUATION_CHARS = list(string.punctuation)

used_passwords = set("PassWord@1 PyBit$s9".split())


___ validate_password(password: str) -> bool:
    __ not (6 <= le.(password) <= 12
        r_ False
    __ password in used_passwords:
        r_ False
    digits = lcase = ucase = punc = 0
    ___ c in password:
        __ c.isdigit(
            digits += 1
        ____ c.islower(
            lcase += 1
        ____ c.isupper(
            ucase += 1
        ____ c in PUNCTUATION_CHARS:
            punc += 1
    __ digits > 0 and lcase > 1 and ucase > 0 and punc > 0:
        used_passwords.add(password)
        r_ True
    r_ False
