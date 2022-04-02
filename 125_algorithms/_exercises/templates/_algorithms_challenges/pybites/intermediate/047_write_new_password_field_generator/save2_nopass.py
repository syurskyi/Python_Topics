_______ s__
_______ __

PUNCTUATION_CHARS = l..(s__.punctuation)

used_passwords = s..('PassWord@1 PyBit$s9'.s..())


___ validate_password(password
    c = __.c..(
        r'^(?=.*\d)(?=.*[a-z]{2,})(?=.*[A-Z])(?=.*[PUNCTUATION_CHARS])[\w\dPUNCTUATION_CHARS]{6,12}$')
    s = __.s..(c, password)
    __ password n.. __ used_passwords a.. b..(s
        used_passwords.add(password)
        r.. b..(s)
    ____:
        r.. F..