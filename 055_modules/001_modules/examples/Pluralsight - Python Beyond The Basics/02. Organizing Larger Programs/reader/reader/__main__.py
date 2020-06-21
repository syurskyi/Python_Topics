import sys

import reader

print ('executing __main__.py with name {}'.format(__name__))

r = reader.Reader(sys.argv[1])
try:
    print(r.read())
finally:
    r.close()