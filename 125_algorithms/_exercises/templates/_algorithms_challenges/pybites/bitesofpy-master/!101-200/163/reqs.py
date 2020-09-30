___ version_newer(old, new
    o = [int(v) ___ v __ old.split('.')]
    n = [int(v) ___ v __ new.split('.')]
    __ o[0] < n[0]:
        r_ True
    ____ o[0] __ n[0]:
        __ o[1] < n[1]:
            r_ True
        ____ o[1] __ n[1]:
            __ o[2] < n[2]:
                r_ True
    r_ False


___ changed_dependencies(old_reqs: str, new_reqs: str) -> list:
    """Compare old vs new requirement multiline strings
       and return a list of dependencies that have been upgraded
       (have a newer version)
    """
    old = [x.split('==') ___ x __ (old_reqs.splitlines(keepends=False)) __ le.(x.strip()) > 0]
    new = [x.split('==') ___ x __ (new_reqs.splitlines(keepends=False)) __ le.(x.strip()) > 0]
    ___ o, n __ zip(old, new
        __ version_newer(o[1], n[1]
            yield n[0]
