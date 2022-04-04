___ version_newer(old, new
    o = [i..(v) ___ v __ old.s..('.')]
    n = [i..(v) ___ v __ new.s..('.')]
    __ o[0] < n[0]:
        r.. T..
    ____ o[0] __ n[0]:
        __ o[1] < n[1]:
            r.. T..
        ____ o[1] __ n[1]:
            __ o[2] < n[2]:
                r.. T..
    r.. F..


___ changed_dependencies(old_reqs: s.., new_reqs: s..) __ l..:
    """Compare old vs new requirement multiline strings
       and return a list of dependencies that have been upgraded
       (have a newer version)
    """
    old = [x.s..('==') ___ x __ (old_reqs.s..k.._F.. __ l..(x.strip > 0]
    new = [x.s..('==') ___ x __ (new_reqs.s..k.._F.. __ l..(x.strip > 0]
    ___ o, n __ z..(old, new
        __ version_newer(o[1], n[1]
            y.. n[0]
