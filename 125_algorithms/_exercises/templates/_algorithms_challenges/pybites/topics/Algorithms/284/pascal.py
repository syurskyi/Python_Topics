____ t___ _______ L..


___ pascal(N: i..) __ L..[i..]:
    """
    Return the Nth row of Pascal triangle
    """
    in_list = [1]
    out_list    # list
    __ N __ 0:
        r.. out_list
    ____ N __ 1:
        r.. in_list
    ____:
        ___ x __ r..(N-1
            #print(x)
            out_list    # list
            ___ i, v __ e..(in_list
                __ i __ 0:
                    out_list.a..(v)
                ____:
                    out_list.a..(v + in_list[i-1])
            out_list.a..(in_list[-1])
            in_list = out_list
    r.. out_list


print(pascal(12