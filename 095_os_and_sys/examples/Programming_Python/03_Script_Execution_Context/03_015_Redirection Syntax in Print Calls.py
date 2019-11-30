import sys
# print(stuff, file=afile) # afile is an object, not a string name
#
import sys
print('spam' * 2, file=sys.stderr)
#
from io import StringIO
buff = StringIO()
print(42, file=buff)
print('spam', file=buff)
print(buff.getvalue())
# 42
# spam
from redirect import Output
buff = Output()
print(43, file=buff)
print('eggs', file=buff)
print(buff.text)
# 43
# eggs