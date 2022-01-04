____ packaging _______ version


___ _load_reqs(reqs: s..) __ d..:
    '''loads reqs into a dict with keys of package names
       and values of version numbers (converted to base 10 equivs)
    '''
    print(f'{reqs.splitlines()=}')
    lines = map(l.... x: x.s..('=='), reqs.splitlines())
    reqs = {x[0]: version.parse(x[1]) ___ x __ lines __ x[0]}
    r.. reqs


___ changed_dependencies(old_reqs: s.., new_reqs: s..) __ l..:
    """Compare old vs new requirement multiline strings
       and return a list of dependencies that have been upgraded
       (have a newer version)
    """
    old, new = _load_reqs(old_reqs), _load_reqs(new_reqs)
    print(f'{old=}\n{new=}')
    r.. [pkg ___ pkg __ new __ new.get(pkg) > old.get(pkg)]
