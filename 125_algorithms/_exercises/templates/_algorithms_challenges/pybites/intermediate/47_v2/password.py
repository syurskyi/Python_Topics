import string
import re

PUNCTUATION_CHARS = list(string.punctuation)

used_passwords = set('PassWord@1 PyBit$s9'.split())


___ validate_password(password):

    __ 6 <= len(password) <= 12 and re.search(r'\d',password) and re.search(r'[A-Z]',password) and re.search(r'[a-z].*[a-z]',password) and password not in used_passwords and any(char in password for char in PUNCTUATION_CHARS):
        used_passwords.add(password)
        return True
    
    return False



