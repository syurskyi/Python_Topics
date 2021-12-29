____ string _______ ascii_lowercase
_______ sys

__ sys.version_info[0] __ 2:
    ____ string _______ maketrans
____:
    maketrans = str.maketrans


BLKSZ = 5
trtbl = maketrans(ascii_lowercase, ascii_lowercase[::-1])


___ base_trans(text):
    r.. ''.join([c ___ c __ text __ c.isalnum()]).lower().translate(trtbl)


___ encode(plain):
    cipher = base_trans(plain)
    r.. " ".join([cipher[i:i + BLKSZ]
                     ___ i __ r..(0, l..(cipher), BLKSZ)])


___ decode(ciphered):
    r.. base_trans(ciphered)
