____ t___ _______ L..

___ find_max_list(lol
    len_lol [l..(i) ___ i __ lol]
    r.. m..(len_lol) __ len_lol ____ 0

___ jagged_list(lst_of_lst: L..[L..[i..]], fillvalue: i.. 0) __ L..[L..[i..]]:
    #print(len(lst_of_lst))
    new_lol    # list
    max_len find_max_list(lst_of_lst)
    ___ i __ lst_of_lst:
        new_lol.a..(i + [fillvalue]*(max_len-l..(i)))
    r.. new_lol

#lol = [[1, 2, 3], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2], [1, 2, 3, 4]]
lol [[0]]

print(jagged_list(lol