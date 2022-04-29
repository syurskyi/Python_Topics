import logging
from pprint import pprint
from sys import stdout as STDOUT


# Example 4
def to_str(unicode_or_str):
    if isinstance(unicode_or_str, unicode):
        value = unicode_or_str.encode('utf-8')
    else:
        value = unicode_or_str
    return value  # Instance of str

print(repr(to_str(u'foo')))
print(repr(to_str('foo')))
