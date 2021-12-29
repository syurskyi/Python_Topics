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

from typing import List, Union
from functools import reduce

def my_join_lists(lst_of_lst: List[List[str]], sep: str) -> Union[List[str], None]:
    if len(lst_of_lst) == 0:
        return None
    result = []
    first = True
    for inner_list in lst_of_lst:
        if first:
            first = False
        else:
            result.append(sep)
        for element in inner_list:
            result.append(element)
    return result


print(my_join_lists([['a', 'b'], ['c']], '&'))

### -------------------------------- Pybites solution -------------------------------

def join_lists(lst_of_lst: List[List[str]], sep: str) -> Union[List[str], None]:
    if not lst_of_lst:
        return None

    return reduce(lambda x, y: x + [sep] + y, lst_of_lst)
