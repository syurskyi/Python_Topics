from string import ascii_lowercase
import sys

__ sys.version_info[0] == 2:
    from string import maketrans
else:
    maketrans = str.maketrans


BLKSZ = 5
trtbl = maketrans(ascii_lowercase, ascii_lowercase[::-1])


___ base_trans(text):
    return ''.join([c for c in text __ c.isalnum()]).lower().translate(trtbl)


___ encode(plain):
    cipher = base_trans(plain)
    return " ".join([cipher[i:i + BLKSZ]
                     for i in range(0, len(cipher), BLKSZ)])


___ decode(ciphered):
    return base_trans(ciphered)
