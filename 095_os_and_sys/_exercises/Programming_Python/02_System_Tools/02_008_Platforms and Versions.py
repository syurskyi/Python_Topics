import sys

print(sys.platform, sys.maxsize, sys.version)
# ('win32', 2147483647, '3.1.1 (r311:74483, Aug 17 2009, 17:02:12) ...more deleted...')
# ######################################################################################################################

if sys.platform[:3] == 'win': print('hello windows')

# hello windows