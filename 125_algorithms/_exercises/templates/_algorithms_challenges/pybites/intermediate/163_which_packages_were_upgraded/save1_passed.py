___ changed_dependencies(old_reqs: str, new_reqs: str) -> l..:
    """Compare old vs new requirement multiline strings
       and return a list of dependencies that have been upgraded
       (have a newer version)
    """
    old = {}
    new = {}
    ___ entry __ old_reqs.strip().split('\n'):
        x = entry.split('==')
        y    # list

        ___ i __ x[1].split('.'):
            __ l..(i) __ 1:
                y.a..('0' + str(i))
            ____:
                y.a..(str(i))

        old[x[0]] = ''.join(y)

    ___ entry __ new_reqs.strip().split('\n'):
        x = entry.split('==')
        y    # list

        ___ i __ x[1].split('.'):
            __ l..(i) __ 1:
                y.a..('0' + str(i))
            ____:
                y.a..(str(i))
        new[x[0]] = ''.join(y)

    output    # list
    ___ k1, v1 __ old.items():
        ___ k2, v2 __ new.items():
            __ k1 __ k2:
                __ l..(v1) > l..(v2):
                    v1 = v1[:l..(v2)]
                    __ int(v2) > int(v1):
                        output.a..(k1)
                ____ l..(v2) > l..(v1):
                    v2 = v2[:l..(v1)]
                    __ int(v2) > int(v1):
                        output.a..(k1)
                ____ l..(v1) __ l..(v2):
                    __ int(v2) > int(v1):
                        output.a..(k1)

    r.. output