_______ string
_______ __

PUNCTUATION_CHARS = l..(string.punctuation)

used_passwords = set('PassWord@1 PyBit$s9'.s..())


___ validate_password(password):

    __ 6 <= l..(password) <= 12 a.. __.s..(r'\d',password) a.. __.s..(r'[A-Z]',password) a.. __.s..(r'[a-z].*[a-z]',password) a.. password n.. __ used_passwords a.. any(char __ password ___ char __ PUNCTUATION_CHARS):
        used_passwords.add(password)
        r.. T..
    
    r.. F..



