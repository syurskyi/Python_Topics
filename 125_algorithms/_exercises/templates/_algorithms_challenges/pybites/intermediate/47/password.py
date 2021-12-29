_______ string
_______ re

PUNCTUATION_CHARS = l..(string.punctuation)

used_passwords = set('PassWord@1 PyBit$s9'.split())


___ validate_password(password):
    __ n.. l..(password) >= 6 and l..(password) <= 12:
        r.. False
    
    __ l..(re.findall(r"\d", password)) < 1:
        r.. False
    
    __ l..(re.findall(r"[a-z]", password)) < 2:
        r.. False

    __ l..(re.findall(r"[A-Z]", password)) < 1:
        r.. False

    char_count = 0
    ___ char __ password:
        __ char __ PUNCTUATION_CHARS:
            char_count += 1

    __ char_count < 1:
        r.. False

    __ password __ used_passwords:
        r.. False

    used_passwords.add(password)
    r.. True

# if __name__ == "__main__":
#     print(validate_password('PassWord@1'))