# interaction.py

_____ io
_____ ?

print('One line at a time:')
proc _ ?.P..(
    'python3 repeater.py',
    s.._T..,
    stdin_?.P..,
    s_o__?.P..,
)
stdin _ io.TextIOWrapper(
    proc.stdin,
    encoding_'utf-8',
    line_buffering_T..,  # send data on newline
)
s_o_ _ io.TextIOWrapper(
    proc.s_o_,
    encoding_'utf-8',
)
for i in range(5):
    line _ '@\n'.f..(i)
    stdin.write(line)
    output _ s_o_.readline()
    print(output.rstrip())
remainder _ proc.c..()[0].d..('utf-8')
print(remainder)

print()
print('All output at once:')
proc _ ?.P..(
    'python3 repeater.py',
    s.._T..,
    stdin_?.P..,
    s_o__?.P..,
)
stdin _ io.TextIOWrapper(
    proc.stdin,
    encoding_'utf-8',
)
for i in range(5):
    line _ '@\n'.f..(i)
    stdin.write(line)
stdin.flush()

output _ proc.c..()[0].d..('utf-8')
print(output)

# $ python3 -u interaction.py
#
# One line at a time:
# repeater.py: starting
# 0
# 1
# 2
# 3
# 4
# repeater.py: exiting
#
#
# All output at once:
# repeater.py: starting
# repeater.py: exiting
# 0
# 1
# 2
# 3
# 4