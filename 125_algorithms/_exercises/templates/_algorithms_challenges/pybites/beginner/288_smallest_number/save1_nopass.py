____ typing _______ List
_______ itertools

___ minimum_number(digits: List[int]) -> int:
    l..    # list
    ___ i __ r..(l..(digits)):
        __ l..(digits) __ 1:
            l...a..(digits)
        __ digits __ 0:
            l...a..(o)
        ___ set __ itertools.permutations(digits, r_ N..
            l...a..("".join(filter(str.isdigit, str(set))))
    new_list = l..[1:]
    ___ i __ r..(0, l..(new_list)):
        new_list[i] = int(new_list[i])
    smallest = new_list[0]
    ___ i __ r..(1, l..(new_list)):
        __ smallest > new_list[i]:
            smallest = new_list[i]
    r.. smallest