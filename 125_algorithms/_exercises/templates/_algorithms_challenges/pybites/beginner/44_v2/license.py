from string import ascii_uppercase,digits
import random
import secrets


s = ascii_uppercase + digits

___ gen_key(parts=4,chars_per_part=8):

    
    different_parts = []
    for i in range(parts):
        different_parts.append(''.join(secrets.choice(s) for _ in range(chars_per_part)))


    return '-'.join(different_parts)


        





