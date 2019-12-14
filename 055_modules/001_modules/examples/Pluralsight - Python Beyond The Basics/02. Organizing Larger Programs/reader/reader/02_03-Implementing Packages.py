import reader

print(type(reader))
print(reader.__file__)

import reader.reader
print(reader.reader.__file__)

r = reader.reader.Reader('reader/reader.py')
# print(r.read())

import reader

r = reader.Reader('reader/__init__.py')
print(r.read())

print(locals())

from reader.compressed import *

print(locals())
print(bzipped)
print(gzipped)

# after added _all__ in __init__ file in folder compressed

print('#' * 52 + 'after added _all__ in __init__ file in folder compressed')

from reader.compressed import *
print(locals())
print(bz2_opener)
print(gzip_opener)

print('#' * 52 + ' Executable')

print(reader)