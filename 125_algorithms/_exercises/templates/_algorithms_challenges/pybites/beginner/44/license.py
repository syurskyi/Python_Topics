_______ string
_______ secrets

___ gen_key(parts=4, chars_per_part=8):
    alphabet = string.ascii_uppercase + string.digits
    segment = [''.join(secrets.choice(alphabet) ___ i __ r..(chars_per_part)) ___ j __ r..(parts)]
    r.. ('-'.join(part ___ part __ segment))

#print(gen_key(parts=8, chars_per_part=2))