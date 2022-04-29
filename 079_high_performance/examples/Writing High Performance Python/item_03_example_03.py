import logging
from pprint import pprint
from sys import stdout as STDOUT


# Example 3
def to_unicode(unicode_or_str):
    if isinstance(unicode_or_str, str):
        value = unicode_or_str.decode('utf-8')
    else:
        value = unicode_or_str
    return value  # Instance of unicode

print(repr(to_unicode(u'foo')))
print(repr(to_unicode('foo')))
