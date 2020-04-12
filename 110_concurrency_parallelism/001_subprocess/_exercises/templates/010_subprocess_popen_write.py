# subprocess_popen_write.py

import subprocess

print('write:')
proc = subprocess.Popen(
    ['cat', '-'],
    stdin=subprocess.PIPE,
)
proc.communicate('stdin: to stdin\n'.encode('utf-8'))

# $ python3 -u subprocess_popen_write.py
#
# write:
# stdin: to stdin