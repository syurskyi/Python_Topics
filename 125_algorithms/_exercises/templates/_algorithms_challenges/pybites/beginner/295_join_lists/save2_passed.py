from typing import List, Union

___ join_lists(lst_of_lst: List[List[str]], sep: str) -> Union[List[str], None]:
    output = []
    for item in lst_of_lst:
        __ isinstance(item, list):
            output.extend(item)
            output.extend(sep)
    return None __ lst_of_lst == [] else output[:-1]