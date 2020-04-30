# subprocess_popen_read.py

_____ ?

print('read:')
proc _ ?.Popen(
    ['echo', '"to stdout"'],
    s_o__?.P..,
)
s_o__value _ proc.communicate()[0].d..('utf-8')
print('stdout:', repr(s_o__value))

# $ python3 subprocess_popen_read.py
#
# read:
# stdout: '"to stdout"\n'

