from string ______ ascii_lowercase
______ sys

__ sys.version_info[0] __ 2:
    from string ______ maketrans
____
    maketrans = str.maketrans


BLKSZ = 5
trtbl = maketrans(ascii_lowercase, ascii_lowercase[::-1])


___ base_trans(text
    r_ ''.join([c ___ c in text __ c.isalnum()]).lower().translate(trtbl)


___ encode(plain
    cipher = base_trans(plain)
    r_ " ".join([cipher[i:i + BLKSZ]
                     ___ i in range(0, le.(cipher), BLKSZ)])


___ decode(ciphered
    r_ base_trans(ciphered)
