import os
for (dirname, subshere, fileshere) in os.walk('.'):
    print('[' + dirname + ']')
    for fname in fileshere:
        print(os.path.join(dirname, fname)) # handle one file

# [.]
# .\random.bin
# .\spam.txt
# .\temp.bin
# .\temp.txt
# [.\parts]
# .\parts\part0001
# .\parts\part0002
# .\parts\part0003
# .\parts\part0004
#
# C:\...\PP4E\System\Filetools> python lister_walk.py C:\temp\test
# [C:\temp\test]
# C:\temp\test\random.bin
# C:\temp\test\spam.txt
# C:\temp\test\temp.bin
# C:\temp\test\temp.txt
# [C:\temp\test\parts]
# C:\temp\test\parts\part0001
# C:\temp\test\parts\part0002
# C:\temp\test\parts\part0003
# C:\temp\test\parts\part0004
# ######################################################################################################################

import os
matches = []
for (dirname, dirshere, fileshere) in os.walk(r'C:\temp\PP3E\Examples'):
    for filename in fileshere:
        if filename.endswith('.py'):
            pathname = os.path.join(dirname, filename)
        if 'mimetypes' in open(pathname).read():
            matches.append(pathname)

for name in matches: print(name)

# C:\temp\PP3E\Examples\PP3E\Internet\Email\mailtools\mailParser.py
# C:\temp\PP3E\Examples\PP3E\Internet\Email\mailtools\mailSender.py
# C:\temp\PP3E\Examples\PP3E\Internet\Ftp\mirror\downloadflat.py
# C:\temp\PP3E\Examples\PP3E\Internet\Ftp\mirror\downloadflat_modular.py
# C:\temp\PP3E\Examples\PP3E\Internet\Ftp\mirror\ftptools.py
# C:\temp\PP3E\Examples\PP3E\Internet\Ftp\mirror\uploadflat.py
# C:\temp\PP3E\Examples\PP3E\System\Media\playfile.py
# ######################################################################################################################

gen = os.walk(r'C:\temp\test')
gen.__next__()
# ('C:\\temp\\test', ['parts'], ['random.bin', 'spam.txt', 'temp.bin', 'temp.txt'])
gen.__next__()
# ('C:\\temp\\test\\parts', [], ['part0001', 'part0002', 'part0003', 'part0004'])
gen.__next__()
# Traceback (most recent call last):
# File "<stdin>", line 1, in <module>
# StopIteration
# ######################################################################################################################

