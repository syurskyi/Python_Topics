_______ s__
_______ __

PUNCTUATION_CHARS l..(s__.p..
used_passwords s..('PassWord@1 PyBit$s9'.s..

___ validate_password_1(password
    __ l.. ? < 6 o. l.. ? > 12:
        r.. F..
    __ n.. a__(elem __ password ___ elem __ s__.a..
        r.. F..
    __ n.. a__(elem __ password ___ elem __ s__.a..
        r.. F..
    __ n.. a__(elem __ password ___ elem __ PUNCTUATION_CHARS
        r.. F..
    __ password __ used_passwords:
        r.. F..

    used_passwords.add ?
    r.. T..

___ validate_password_2(password
    __ l.. ? < 6 o. l.. ? > 12:
        r.. F..
    __ n.. __.s.. _ [0-9]', password
        r.. F..
    __ n.. __.s.. _ [a-z]', password
        r.. F..
    __ n.. __.s.. _ [A-Z]', password
        r.. F..
    __ n.. a__(elem __ password ___ elem __ PUNCTUATION_CHARS
        r.. F..
    __ password __ used_passwords:
        r.. F..

    used_passwords.add ?
    r.. T..

validate_password("passWord9_")