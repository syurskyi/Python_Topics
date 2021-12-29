import os
from tempfile import TemporaryDirectory


TMP = 'tmp'
ONE_KB = 1024



___ get_files(dirname, size_in_kb):
    """Return files in dirname that are >= size_in_kb"""

    result = []
    print(dirname)
    for file in os.listdir(dirname):
        __ os.path.isfile(os.path.join(dirname,file)):
            size = os.path.getsize(os.path.join(dirname,file))
            print(file,size)
            size /= ONE_KB
            __ size >= size_in_kb:
                yield file




