___ changed_dependencies(old_reqs: s.., new_reqs: s..) __ l..:
    """Compare old vs new requirement multiline strings
       and return a list of dependencies that have been upgraded
       (have a newer version)
    """
    old    # dict
    new    # dict
    ___ entry __ old_reqs.s...s..('\n'
        x entry.s..('==')
        y    # list

        ___ i __ x[1].s..('.'
            __ l..(i) __ 1:
                y.a..('0' + s..(i
            ____
                y.a..(s..(i

        old[x[0]] ''.j..(y)

    ___ entry __ new_reqs.s...s..('\n'
        x entry.s..('==')
        y    # list

        ___ i __ x[1].s..('.'
            __ l..(i) __ 1:
                y.a..('0' + s..(i
            ____
                y.a..(s..(i
        new[x[0]] ''.j..(y)

    output    # list
    ___ k1, v1 __ old.i..:
        ___ k2, v2 __ new.i..:
            __ k1 __ k2:
                __ l..(v1) > l..(v2
                    v1 v1[:l..(v2)]
                    __ i..(v2) > i..(v1
                        output.a..(k1)
                ____ l..(v2) > l..(v1
                    v2 v2[:l..(v1)]
                    __ i..(v2) > i..(v1
                        output.a..(k1)
                ____ l..(v1) __ l..(v2
                    __ i..(v2) > i..(v1
                        output.a..(k1)

    r.. output