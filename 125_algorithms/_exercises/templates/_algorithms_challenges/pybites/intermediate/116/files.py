_______ os
_______ glob

ONE_KB = 1024


___ get_files(dirname, size_in_kb):
    """Return files in dirname that are >= size_in_kb"""
    file_gt_kb    # list
    ___ file __ glob.glob(f"{dirname}/*"):
        file_size = os.path.getsize(file)
        __ file_size >= (size_in_kb * ONE_KB):
            file_gt_kb.a..(str(file_size))

    r.. file_gt_kb