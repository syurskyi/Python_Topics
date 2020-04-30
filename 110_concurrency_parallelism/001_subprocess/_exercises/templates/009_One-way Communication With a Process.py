# subprocess_popen_read.py

_____ ?

print('read:')
proc _ ?.Popen(
    ['echo', '"to stdout"'],
    stdout_?.PIPE,
)
stdout_value _ proc.communicate()[0].decode('utf-8')
print('stdout:', repr(stdout_value))

# $ python3 subprocess_popen_read.py
#
# read:
# stdout: '"to stdout"\n'

