# c:\temp> dir /B
# parts
# PP3E
# random.bin
# spam.txt
# temp.bin
# temp.txt
# c:\temp> c:\cygwin\bin\ls
# PP3E parts random.bin spam.txt temp.bin temp.txt
# c:\temp> c:\cygwin\bin\ls parts
# part0001 part0002 part0003 part0004
#
# C:\temp> python
import os
os.popen('dir /B').readlines()
# ['parts\n', 'PP3E\n', 'random.bin\n', 'spam.txt\n', 'temp.bin\n', 'temp.txt\n']
# ######################################################################################################################

for line in os.popen('dir /B'):
    print(line[:-1])

# parts
# PP3E
# random.bin
# spam.txt
# temp.bin
# temp.txt
# ######################################################################################################################

lines = [line[:-1] for line in os.popen('dir /B')]
lines
# ['parts', 'PP3E', 'random.bin', 'spam.txt', 'temp.bin', 'temp.txt']
# ######################################################################################################################

os.popen('dir *.bin /B').readlines()
# ['random.bin\n', 'temp.bin\n']
# ######################################################################################################################

os.popen(r'c:\cygwin\bin\ls *.bin').readlines()
# ['random.bin\n', 'temp.bin\n']
# ######################################################################################################################

list(os.popen(r'dir parts /B'))
# ['part0001\n', 'part0002\n', 'part0003\n', 'part0004\n']
# ######################################################################################################################

[fname for fname in os.popen(r'c:\cygwin\bin\ls parts')]
# ['part0001\n', 'part0002\n', 'part0003\n', 'part0004\n']
# ######################################################################################################################

list(os.popen(r'dir parts\part* /B'))
# ['part0001\n', 'part0002\n', 'part0003\n', 'part0004\n']
# ######################################################################################################################
