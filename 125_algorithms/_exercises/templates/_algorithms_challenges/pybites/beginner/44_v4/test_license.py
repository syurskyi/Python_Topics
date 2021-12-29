_______ re

____ Previous.license _______ gen_key

default_key = re.compile(r'^([A-Z0-9]{8}-){3}[A-Z0-9]{8}$')
shorter_key = re.compile(r'^([A-Z0-9]{4}-){2}[A-Z0-9]{4}$')
longer_key = re.compile(r'^([A-Z0-9]{10}-){9}[A-Z0-9]{10}$')


___ test_gen_default_key():
    ... default_key.match(gen_key())


___ test_gen_shorter_key():
    ... shorter_key.match(gen_key(parts=3, chars_per_part=4))


___ test_gen_longer_key():
    ... longer_key.match(gen_key(parts=10, chars_per_part=10))