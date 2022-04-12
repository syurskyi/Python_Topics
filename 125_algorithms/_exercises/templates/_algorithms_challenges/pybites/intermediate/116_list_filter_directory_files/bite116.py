_______ __

ONE_KB 1024


___ get_files(dirname, size_in_kb
    """Return files in dirname that are >= size_in_kb"""
    output    # list
    ___ root, dirs, files __ __.w..(dirname, topdown=F..
        ___ name __ ?
            f __.p...j..(root, name)
            size __.p...getsize(f) / ONE_KB
            __  size >_ size_in_kb:
                ?.a.. f)
    r.. ?