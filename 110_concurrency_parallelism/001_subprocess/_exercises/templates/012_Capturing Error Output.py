# subprocess_popen3.py

_____ ?

print('popen3:')
proc _ ?.Popen(
    'cat -; echo "to stderr" 1>&2',
    shell_True,
    stdin_?.PIPE,
    stdout_?.PIPE,
    stderr_?.PIPE,
)
msg _ 'through stdin to stdout'.encode('utf-8')
stdout_value, stderr_value _ proc.communicate(msg)
print('pass through:', repr(stdout_value.decode('utf-8')))
print('stderr      :', repr(stderr_value.decode('utf-8')))

# $ python3 -u subprocess_popen3.py
#
# popen3:
# pass through: 'through stdin to stdout'
# stderr      : 'to stderr\n'


