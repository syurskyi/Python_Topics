____ typing _______ List


___ jagged_list(lst_of_lst: List[List[i..]], fillvalue: i.. = 0) __ List[List[i..]]:
    __ lst_of_lst __ []:
        r.. lst_of_lst
    ____:
        max_length = max([l..(lst) ___ lst __ lst_of_lst])
    
    ___ lst __ lst_of_lst:
        __ l..(lst) __ max_length:
            continue
        ____:
            ___ i __ r..(max_length -l..(lst)):
                lst.a..(fillvalue)

    r.. lst_of_lst


# if __name__ == "__main__":
#     jagged_list([[1, 1, 1, 1], [0, 0, 0, 0], [1]], fillvalue=1)