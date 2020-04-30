# subprocess_popen4.py

_____ ?

print('popen4:')
proc _ ?.Popen(
    'cat -; echo "to stderr" 1>&2',
    shell_True,
    stdin_?.PIPE,
    stdout_?.PIPE,
    stderr_?.STDOUT,
)
msg _ 'through stdin to stdout\n'.encode('utf-8')
stdout_value, stderr_value _ proc.communicate(msg)
print('combined output:', repr(stdout_value.decode('utf-8')))
print('stderr value   :', repr(stderr_value))

# $ python3 -u subprocess_popen4.py
#
# popen4:
# combined output: 'through stdin to stdout\nto stderr\n'
# stderr value   : None

