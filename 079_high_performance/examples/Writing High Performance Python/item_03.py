import logging
from pprint import pprint
from sys import stdout as STDOUT


# Example 1
def to_str(bytes_or_str):
    if isinstance(bytes_or_str, bytes):
        value = bytes_or_str.decode('utf-8')
    else:
        value = bytes_or_str
    return value  # Instance of str

print(repr(to_str(b'foo')))
print(repr(to_str('foo')))


# Example 2
def to_bytes(bytes_or_str):
    if isinstance(bytes_or_str, str):
        value = bytes_or_str.encode('utf-8')
    else:
        value = bytes_or_str
    return value  # Instance of bytes

print(repr(to_bytes(b'foo')))
print(repr(to_bytes('foo')))


# Example 5
try:
    import os
    with open('random.bin', 'w') as f:
        f.write(os.urandom(10))
except:
    logging.exception('Expected')
else:
    assert False


# Example 6
with open('random.bin', 'wb') as f:
    f.write(os.urandom(10))
