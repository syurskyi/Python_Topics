_______ os
____ tempfile _______ TemporaryDirectory


TMP = 'tmp'
ONE_KB = 1024



___ get_files(dirname, size_in_kb):
    """Return files in dirname that are >= size_in_kb"""

    result    # list
    print(dirname)
    ___ file __ os.listdir(dirname):
        __ os.path.isfile(os.path.j..(dirname,file)):
            size = os.path.getsize(os.path.j..(dirname,file))
            print(file,size)
            size /= ONE_KB
            __ size >= size_in_kb:
                y.. file




