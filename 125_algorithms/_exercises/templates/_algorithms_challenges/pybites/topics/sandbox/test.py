level = 4

in_list = [1]

___ pascal_next(in_list):
    out_list    # list
    ___ i, v __ e..(in_list):
        __ i __ 0:
            out_list.a..(v)
        ____:
            out_list.a..(v + in_list[i-1])
    out_list.a..(in_list[-1])
    r.. out_list

___ i __ r..(0):
    in_list = pascal_next(in_list)

print(in_list)