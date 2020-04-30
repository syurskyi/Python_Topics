# subprocess_popen4.py

_____ ?

print('popen4:')
proc _ ?.Popen(
    'cat -; echo "to stderr" 1>&2',
    s.._T..,
    stdin_?.P..,
    s_o__?.P..,
    stderr_?.STDOUT,
)
msg _ 'through stdin to stdout\n'.encode('utf-8')
s_o__value, stderr_value _ proc.communicate(msg)
print('combined output:', repr(s_o__value.d..('utf-8')))
print('stderr value   :', repr(stderr_value))

# $ python3 -u subprocess_popen4.py
#
# popen4:
# combined output: 'through stdin to stdout\nto stderr\n'
# stderr value   : None

