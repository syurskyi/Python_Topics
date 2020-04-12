# subprocess_popen_read.py

import subprocess

print('read:')
proc = subprocess.Popen(
    ['echo', '"to stdout"'],
    stdout=subprocess.PIPE,
)
stdout_value = proc.communicate()[0].decode('utf-8')
print('stdout:', repr(stdout_value))

# $ python3 subprocess_popen_read.py
#
# read:
# stdout: '"to stdout"\n'

