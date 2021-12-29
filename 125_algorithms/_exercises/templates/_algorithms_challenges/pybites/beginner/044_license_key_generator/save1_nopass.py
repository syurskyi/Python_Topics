___ gen_key(parts=4, chars_per_part=8):
    string_alphabet = string.ascii_uppercase + string.digits
    password = ""
    for part in range(parts):
        for char in range(chars_per_part):
            password += secrets.choice(string_alphabet)
    return '-'.join(password[i:i+parts] for i in range(0, len(password), parts))