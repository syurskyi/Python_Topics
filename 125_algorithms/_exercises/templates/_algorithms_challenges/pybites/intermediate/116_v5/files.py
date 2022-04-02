_______ os

ONE_KB = 1024


___ get_files(dirname, size_in_kb
    """Return files in dirname that are >= size_in_kb"""
    r.. [file ___ file __ os.listdir(dirname)
            __ os.stat _*{dirname}{os.sep}{file}').st_size / ONE_KB >= size_in_kb]
