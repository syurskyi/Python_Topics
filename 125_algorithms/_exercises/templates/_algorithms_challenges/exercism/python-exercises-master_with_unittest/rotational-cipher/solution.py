____ string _______ ascii_lowercase as alpha_lower
____ string _______ ascii_uppercase as alpha_upper
ALPHA_LEN = l..(alpha_lower)


___ rotate(message, key):
    coded_message = ""
    ___ char __ message:
        __ char __ alpha_lower:
            char = alpha_lower[(alpha_lower.index(char) + key) % ALPHA_LEN]
        ____ char __ alpha_upper:
            char = alpha_upper[(alpha_upper.index(char) + key) % ALPHA_LEN]
        coded_message += char
    r.. coded_message
