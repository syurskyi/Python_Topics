import os
import glob

ONE_KB = 1024


def get_files(dirname, size_in_kb):
    """Return files in dirname that are >= size_in_kb"""
    file_gt_kb = []
    for file in glob.glob(f"{dirname}/*"):
        file_size = os.path.getsize(file)
        if file_size >= (size_in_kb * ONE_KB):
            file_gt_kb.append(str(file_size))

    return file_gt_kb