______ os

ONE_KB = 1024


___ get_files(dirname, size_in_kb
    """Return files in dirname that are >= size_in_kb"""
    r_ [file ___ file in os.listdir(dirname)
            __ os.stat(f'{dirname}{os.sep}{file}').st_size / ONE_KB >= size_in_kb]
