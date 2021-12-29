_______ string
_______ re

PUNCTUATION_CHARS = l..(string.punctuation)

used_passwords = set('PassWord@1 PyBit$s9'.split())


___ validate_password(password):

    __ 6 <= l..(password) <= 12 and re.search(r'\d',password) and re.search(r'[A-Z]',password) and re.search(r'[a-z].*[a-z]',password) and password n.. __ used_passwords and any(char __ password ___ char __ PUNCTUATION_CHARS):
        used_passwords.add(password)
        r.. True
    
    r.. False



