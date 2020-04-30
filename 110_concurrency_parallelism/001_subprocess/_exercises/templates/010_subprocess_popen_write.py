# subprocess_popen_write.py

_____ ?

print('write:')
proc _ ?.Popen(
    ['cat', '-'],
    stdin_?.PIPE,
)
proc.communicate('stdin: to stdin\n'.encode('utf-8'))

# $ python3 -u subprocess_popen_write.py
#
# write:
# stdin: to stdin