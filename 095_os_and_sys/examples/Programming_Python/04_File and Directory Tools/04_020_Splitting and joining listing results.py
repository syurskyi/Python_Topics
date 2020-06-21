dirname = r'C:\temp\parts'

import glob
for file in glob.glob(dirname + '/*'):
    head, tail = os.path.split(file)
    print(head, tail, '=>', ('C:\\Other\\' + tail))

# C:\temp\parts part0001 => C:\Other\part0001
# C:\temp\parts part0002 => C:\Other\part0002
# C:\temp\parts part0003 => C:\Other\part0003
# C:\temp\parts part0004 => C:\Other\part0004
# ######################################################################################################################

import os
for file in os.listdir(dirname):
    print(dirname, file, '=>', os.path.join(dirname, file))

# C:\temp\parts part0001 => C:\temp\parts\part0001
# C:\temp\parts part0002 => C:\temp\parts\part0002
# C:\temp\parts part0003 => C:\temp\parts\part0003
# C:\temp\parts part0004 => C:\temp\parts\part0004
# ######################################################################################################################

