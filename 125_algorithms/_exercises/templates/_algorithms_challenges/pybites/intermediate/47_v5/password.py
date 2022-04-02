_______ s__

PUNCTUATION_CHARS = l..(s__.punctuation)

used_passwords = s..("PassWord@1 PyBit$s9".s..())


___ validate_password(password: s..) __ b..:
    __ n.. (6 <= l..(password) <= 12
        r.. F..
    __ password __ used_passwords:
        r.. F..
    d.. = lcase = ucase = punc = 0
    ___ c __ password:
        __ c.i..
            d.. += 1
        ____ c.isl..
            lcase += 1
        ____ c.isupper
            ucase += 1
        ____ c __ PUNCTUATION_CHARS:
            punc += 1
    __ d.. > 0 a.. lcase > 1 a.. ucase > 0 a.. punc > 0:
        used_passwords.add(password)
        r.. T..
    r.. F..
