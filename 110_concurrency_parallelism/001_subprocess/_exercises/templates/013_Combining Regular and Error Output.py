# subprocess_popen4.py

_____ ?

print('popen4:')
proc _ ?.P..(
    'cat -; echo "to s_e.." 1>&2',
    s.._T..,
    s_i._?.P..,
    s_o__?.P..,
    s_e.._?.S_O..,
)
msg _ 'through s_i. to stdout\n'.e..('utf-8')
s_o__value, s_e.._value _ proc.c..(msg)
print('combined output:', repr(s_o__value.d..('utf-8')))
print('s_e.. value   :', repr(s_e.._value))

# $ python3 -u subprocess_popen4.py
#
# popen4:
# combined output: 'through s_i. to stdout\nto s_e..\n'
# s_e.. value   : None

