# subprocess_popen2.py

_____ ?

print('popen2:')

proc _ ?.Popen(
    ['cat', '-'],
    stdin_?.P..,
    s_o__?.P..,
)
msg _ 'through stdin to stdout'.encode('utf-8')
s_o__value _ proc.communicate(msg)[0].d..('utf-8')
print('pass through:', repr(s_o__value))

# $ python3 -u subprocess_popen2.py
#
# popen2:
# pass through: 'through stdin to stdout'


