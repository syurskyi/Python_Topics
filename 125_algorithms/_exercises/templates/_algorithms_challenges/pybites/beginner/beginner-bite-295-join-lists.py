### Last worked on 11 Oct 2020

"""
Write a function that accepts a list of lists and joins them with a separator character,
therefore flattening and separating.

Examples:

>>> join_lists([ ['a', 'b'], ['c'] ], '&')
['a', 'b', '&', 'c']
>>> join_lists([ ['a', 'b'], ['c'], ['d', 'e'] ], '+')
['a', 'b', '+', 'c', '+', 'd', 'e']
Note: Calling the function with an empty list should return None.

"""

### RESOURCES
### https://realpython.com/python-lambda/


### ----------------------------- My solution -----------------------------------

____ t___ _______ L.., Union
____ f.. _______ r..

___ my_join_lists(lst_of_lst: L..[L..[s..]], sep: s..) __ Union[L..[s..], N..]:
    __ l..(lst_of_lst) __ 0:
        r.. N..
    result    # list
    first = T..
    ___ inner_list __ lst_of_lst:
        __ first:
            first = F..
        ____:
            result.a..(sep)
        ___ element __ inner_list:
            result.a..(element)
    r.. result


print(my_join_lists([['a', 'b' ,  'c']], '&'

### -------------------------------- Pybites solution -------------------------------

___ join_lists(lst_of_lst: L..[L..[s..]], sep: s..) __ Union[L..[s..], N..]:
    __ n.. lst_of_lst:
        r.. N..

    r.. r.. l.... x, y: x + [sep] + y, lst_of_lst)
