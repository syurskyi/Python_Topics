import string
import secrets

def gen_key(parts=4, chars_per_part=8):
    alphabet = string.ascii_uppercase + string.digits
    segment = [''.join(secrets.choice(alphabet) for i in range(chars_per_part)) for j in range(parts)]
    return ('-'.join(part for part in segment))

#print(gen_key(parts=8, chars_per_part=2))