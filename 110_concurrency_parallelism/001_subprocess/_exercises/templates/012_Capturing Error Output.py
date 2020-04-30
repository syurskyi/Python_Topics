# subprocess_popen3.py

_____ ?

print('popen3:')
proc _ ?.Popen(
    'cat -; echo "to stderr" 1>&2',
    s.._T..,
    stdin_?.P..,
    s_o__?.P..,
    stderr_?.P..,
)
msg _ 'through stdin to stdout'.encode('utf-8')
s_o__value, stderr_value _ proc.communicate(msg)
print('pass through:', repr(s_o__value.d..('utf-8')))
print('stderr      :', repr(stderr_value.d..('utf-8')))

# $ python3 -u subprocess_popen3.py
#
# popen3:
# pass through: 'through stdin to stdout'
# stderr      : 'to stderr\n'


