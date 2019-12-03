import sys
for f in (sys.stdin, sys.stdout, sys.stderr): print(f)

# <_io.TextIOWrapper name='<stdin>' encoding='cp437'>
# <_io.TextIOWrapper name='<stdout>' encoding='cp437'>
# <_io.TextIOWrapper name='<stderr>' encoding='cp437'>
# ######################################################################################################################

print('#' * 52)
print('hello stdout world')
# hello stdout world
# ######################################################################################################################

sys.stdout.write('hello stdout world' + '\n')
# hello stdout world
# 19
# ######################################################################################################################

input('hello stdin world>')
# hello stdin world>spam
# 'spam'
# ######################################################################################################################

print('hello stdin world>'); sys.stdin.readline()[:-1]
# hello stdin world>
# eggs
# 'eggs
# ######################################################################################################################