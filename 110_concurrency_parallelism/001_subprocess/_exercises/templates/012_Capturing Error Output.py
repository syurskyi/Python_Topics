# subprocess_popen3.py

_____ ?

print('popen3:')
proc _ ?.P..(
    'cat -; echo "to s_e.." 1>&2',
    s.._T..,
    s_i._?.P..,
    s_o__?.P..,
    s_e.._?.P..,
)
msg _ 'through s_i. to stdout'.e..('utf-8')
s_o__value, s_e.._value _ proc.c..(msg)
print('pass through:', repr(s_o__value.d..('utf-8')))
print('s_e..      :', repr(s_e.._value.d..('utf-8')))

# $ python3 -u subprocess_popen3.py
#
# popen3:
# pass through: 'through s_i. to stdout'
# s_e..      : 'to s_e..\n'


