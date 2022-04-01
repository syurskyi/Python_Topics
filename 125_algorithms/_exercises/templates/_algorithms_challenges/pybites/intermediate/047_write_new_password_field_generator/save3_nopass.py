_______ s__
_______ __

PUNCTUATION_CHARS = l..(s__.punctuation)

used_passwords = s..('PassWord@1 PyBit$s9'.s..())


___ validate_password(password):
    c = __.c..(
        r'^.*(?=.*\d)(?=.*[a-z]{2,})(?=.*[A-Z])[\w\d]{6,12}$')
    s = __.s..(c, password)
    __ (password n.. __ used_passwords) a.. (bool(s) __ T..):
        ___ c __ password:
            __ c __ PUNCTUATION_CHARS:
                used_passwords.add(password)
                r.. bool(s)
    ____:
        r.. F..