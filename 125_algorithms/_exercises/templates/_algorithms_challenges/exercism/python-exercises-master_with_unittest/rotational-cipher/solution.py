____ s__ _______ a.. __ alpha_lower
____ s__ _______ a.. __ alpha_upper
ALPHA_LEN = l..(alpha_lower)


___ rotate(message, key
    coded_message = ""
    ___ char __ message:
        __ char __ alpha_lower:
            char = alpha_lower[(alpha_lower.i.. char) + key) % ALPHA_LEN]
        ____ char __ alpha_upper:
            char = alpha_upper[(alpha_upper.i.. char) + key) % ALPHA_LEN]
        coded_message += char
    r.. coded_message
