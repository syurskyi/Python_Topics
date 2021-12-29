from typing import List, Union

def join_lists(lst_of_lst: List[List[str]], sep: str) -> Union[List[str], None]:
    output = []
    for item in lst_of_lst:
        if isinstance(item, list):
            output.extend(item)
            output.extend(sep)
    return output[:-1]