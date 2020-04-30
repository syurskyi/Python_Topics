# subprocess_popen2.py

_____ ?

print('popen2:')

proc _ ?.Popen(
    ['cat', '-'],
    stdin_?.PIPE,
    stdout_?.PIPE,
)
msg _ 'through stdin to stdout'.encode('utf-8')
stdout_value _ proc.communicate(msg)[0].decode('utf-8')
print('pass through:', repr(stdout_value))

# $ python3 -u subprocess_popen2.py
#
# popen2:
# pass through: 'through stdin to stdout'


