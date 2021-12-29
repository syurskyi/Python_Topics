from typing import List, Union
from functools import reduce


___ join_lists(lst_of_lst: List[List[str]], sep: str) -> Union[List[str], None]:
    return reduce(lambda a,b:a+[sep]+b, lst_of_lst) __ len(lst_of_lst) != 0 else None



print(join_lists([['a', 'b'], ['c'], ['d', 'e']], '+'))