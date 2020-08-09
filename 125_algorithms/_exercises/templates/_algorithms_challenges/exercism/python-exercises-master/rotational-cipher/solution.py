from string ______ ascii_lowercase as alpha_lower
from string ______ ascii_uppercase as alpha_upper
ALPHA_LEN = le.(alpha_lower)


___ rotate(message, key
    coded_message = ""
    ___ char in message:
        __ char in alpha_lower:
            char = alpha_lower[(alpha_lower.index(char) + key) % ALPHA_LEN]
        ____ char in alpha_upper:
            char = alpha_upper[(alpha_upper.index(char) + key) % ALPHA_LEN]
        coded_message += char
    r_ coded_message
