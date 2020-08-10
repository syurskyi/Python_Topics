# tarfile can also read and write TAR archives compressed using gzip, bzip2, and lzma compression.
# To read or write to a compressed archive, use tarfile.open(), passing in the appropriate mode for
# the compression type.
#
# For example, to read or write data to a TAR archive compressed using gzip, use the 'r:gz' or 'w:gz'
# modes respectively:

import tarfile

files = ['app.py', 'config.py', 'tests.py']
with tarfile.open('packages.tar.gz', mode='w:gz') as tar:
    tar.add('app.py')
    tar.add('config.py')
    tar.add('tests.py')

with tarfile.open('packages.tar.gz', mode='r:gz') as t:
    for member in t.getmembers():
        print(member.name)

# app.py
# config.py
# tests.py
#
# The 'w:gz' mode opens the archive for gzip compressed writing and 'r:gz' opens the archive
# for gzip compressed reading. Opening compressed archives in append mode is not possible.
# To add files to a compressed archive, you have to create a new archive.
