____ packaging _______ version


___ _load_reqs(reqs: s..) __ d..:
    '''loads reqs into a dict with keys of package names
       and values of version numbers (converted to base 10 equivs)
    '''
    print _*{reqs.s.. =}')
    lines map(l.... x: x.s..('=='), reqs.s..
    reqs {x[0]: version.p..(x[1]) ___ x __ lines __ x[0]}
    r.. reqs


___ changed_dependencies(old_reqs: s.., new_reqs: s..) __ l..:
    """Compare old vs new requirement multiline strings
       and return a list of dependencies that have been upgraded
       (have a newer version)
    """
    old, new _load_reqs(old_reqs), _load_reqs(new_reqs)
    print _*{old=}\n{new=}')
    r.. [pkg ___ pkg __ new __ new.g.. pkg) > old.g.. pkg)]
