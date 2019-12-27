# -*- coding: utf-8 -*-

import hashlib
h = hashlib.md5(b"password")
p = h.hexdigest()
print(p)                               # Пароль, сохраненный в базе
# '5f4dcc3b5aa765d61d8327deb882cf99'
h2 = hashlib.md5(b"password")    # Пароль, введенный пользователем
if p == h2.hexdigest(): print("Пароль правильный")


h = hashlib.sha512(b"password")
h.digest_size
# 64

import hashlib
dk = hashlib.pbkdf2_hmac('sha512', b'1234567', b'saltsaltsaltsalt', 100000)
print(dk)
# b"Sb\x85tc-\xcb@\xc5\x97\x19\x90\x94@\x9f\xde\x07\xa4p-\x83\x94\xf4\x94\x99\x07\xec\xfa\xf3\xcd\xc3\x88jv\xd1\xe5\x9a\x119\x15/\xa4\xc2\xd3N\xaba\x02\xc0s\xc1\xd1\x0b\x86xj(\x8c>Mr'@\xbb"