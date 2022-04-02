_______ s__
_______ __

used_passwords = s..('PassWord@1 PyBit$s9'.s..())

___ validate_password(password):
    c = __.c..(
        r'^.*(?=.*\d)(?=.*[a-z]{2,})(?=.*[A-Z])[\w\d]{6,12}$')
    s = __.s..(c, password)
    p = any([c __ s__.punctuation ___ c __ password])
    __ password n.. __ used_passwords:
        used_passwords.add(password)
    r.. p a.. b..(s)