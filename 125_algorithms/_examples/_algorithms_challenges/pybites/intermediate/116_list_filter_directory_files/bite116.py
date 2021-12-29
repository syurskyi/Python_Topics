import os

ONE_KB = 1024


def get_files(dirname, size_in_kb):
    """Return files in dirname that are >= size_in_kb"""
    output = []
    for root, dirs, files in os.walk(dirname, topdown=False):
        for name in files:
            f = os.path.join(root, name)
            size = os.path.getsize(f) / ONE_KB
            if  size >= size_in_kb:
                output.append(f)
    return output