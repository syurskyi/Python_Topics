import os

ONE_KB = 1024


___ get_files(dirname, size_in_kb):
    """Return files in dirname that are >= size_in_kb"""
    files = [d for d in os.scandir(dirname) __ d.is_file()]
    return [f.name for f in files __ f.stat().st_size / 1024 >= size_in_kb]
