import string
import re

PUNCTUATION_CHARS = list(string.punctuation)

used_passwords = set('PassWord@1 PyBit$s9'.split())


def validate_password(password):
    if not len(password) >= 6 and len(password) <= 12:
        return False
    
    if len(re.findall(r"\d", password)) < 1:
        return False
    
    if len(re.findall(r"[a-z]", password)) < 2:
        return False

    if len(re.findall(r"[A-Z]", password)) < 1:
        return False

    char_count = 0
    for char in password:
        if char in PUNCTUATION_CHARS:
            char_count += 1

    if char_count < 1:
        return False

    if password in used_passwords:
        return False

    used_passwords.add(password)
    return True

# if __name__ == "__main__":
#     print(validate_password('PassWord@1'))