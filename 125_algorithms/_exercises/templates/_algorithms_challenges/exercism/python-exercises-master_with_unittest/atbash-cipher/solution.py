____ s__ _______ ascii_lowercase
_______ ___

__ ___.version_info[0] __ 2:
    ____ s__ _______ maketrans
____
    maketrans = s...maketrans


BLKSZ = 5
trtbl = maketrans(ascii_lowercase, ascii_lowercase[::-1])


___ base_trans(text
    r.. ''.j..([c ___ c __ text __ c.isalnum()]).l...translate(trtbl)


___ encode(plain
    cipher = base_trans(plain)
    r.. " ".j..([cipher[i:i + BLKSZ]
                     ___ i __ r..(0, l..(cipher), BLKSZ)])


___ d.. ciphered
    r.. base_trans(ciphered)
