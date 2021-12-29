import os

ONE_KB = 1024


def get_files(dirname, size_in_kb):
    """Return files in dirname that are >= size_in_kb"""
    files = [d for d in os.scandir(dirname) if d.is_file()]
    return [f.name for f in files if f.stat().st_size / 1024 >= size_in_kb]
