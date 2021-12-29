_______ secrets
_______ string

___ gen_key(parts=4, chars_per_part=8):
    string_alphabet = string.ascii_uppercase + string.digits
    password = ""
    ___ part __ r..(parts):
        ___ char __ r..(chars_per_part):
            password += secrets.choice(string_alphabet)
    r.. '-'.join(password[i:i+parts] ___ i __ r..(0, l..(password), parts))