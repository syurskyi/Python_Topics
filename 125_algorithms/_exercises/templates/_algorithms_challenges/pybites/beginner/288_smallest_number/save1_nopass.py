____ t___ _______ List
_______ i..

___ minimum_number(d..: List[i..]) __ i..:
    l..    # list
    ___ i __ r..(l..(d..)):
        __ l..(d..) __ 1:
            l...a..(d..)
        __ d.. __ 0:
            l...a..(o)
        ___ s.. __ i...permutations(d.., r_ N..
            l...a..("".j..(f.. s...i.., s..(s..))))
    new_list = l..[1:]
    ___ i __ r..(0, l..(new_list)):
        new_list[i] = i..(new_list[i])
    smallest = new_list[0]
    ___ i __ r..(1, l..(new_list)):
        __ smallest > new_list[i]:
            smallest = new_list[i]
    r.. smallest