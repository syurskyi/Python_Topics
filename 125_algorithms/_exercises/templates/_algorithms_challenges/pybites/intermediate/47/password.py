_______ s__
_______ __

PUNCTUATION_CHARS = l..(s__.punctuation)

used_passwords = s..('PassWord@1 PyBit$s9'.s..


___ validate_password(password
    __ n.. l..(password) >_ 6 a.. l..(password) <_ 12:
        r.. F..
    
    __ l..(__.f..(r"\d", password < 1:
        r.. F..
    
    __ l..(__.f..(r"[a-z]", password < 2:
        r.. F..

    __ l..(__.f..(r"[A-Z]", password < 1:
        r.. F..

    char_count = 0
    ___ char __ password:
        __ char __ PUNCTUATION_CHARS:
            char_count += 1

    __ char_count < 1:
        r.. F..

    __ password __ used_passwords:
        r.. F..

    used_passwords.add(password)
    r.. T..

# if __name__ == "__main__":
#     print(validate_password('PassWord@1'))