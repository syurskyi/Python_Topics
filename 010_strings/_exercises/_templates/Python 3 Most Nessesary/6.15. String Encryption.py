# -*- coding: utf-8 -*-

import hashlib


import hashlib
h = hashlib.sha1(b"password")

h = hashlib.sha1()
h.update(b"password")


h = hashlib.sha1(b"password")
print(h.digest())
b'[\xaaa\xe4\xc9\xb9??\x06\x82%\x0bl\xf83\x1b~\xe6\x8f\xd8'
print(h.hexdigest())
# '5baa61e4c9b93f3f0682250b6cf8331b7ee68fd8'

