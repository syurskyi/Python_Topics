_______ s__
_______ __

PUNCTUATION_CHARS = l..(s__.punctuation)

used_passwords = s..('PassWord@1 PyBit$s9'.s..())

"""
is between 6 and 12 chars long (both inclusive)
has at least 1 digit [0-9]
has at least two lowercase chars [a-z]
has at least one uppercase char [A-Z]
has at least one punctuation char (use: PUNCTUATION_CHARS)
Has not been used before (use: used_passwords)
"""


___ validate_password(password

    length = 6 <= l..(password) <= 12
    digit = l..(__.f..(r'[0-9]', password)) >= 1
    lower = l..(__.f..(r'[a-z]', password)) >= 1
    upper = l..(__.f..(r'[A-Z]', password)) >= 1
    punc = any([c __ PUNCTUATION_CHARS ___ c __ password])
    new = password n.. __ used_passwords

    valid = length a.. digit a.. lower a.. upper a.. punc a.. new

    __ valid:
        used_passwords.add(password)

    r.. valid
