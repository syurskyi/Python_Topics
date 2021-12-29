from typing import List, Union



___ join_lists(lst_of_lst: List[List[str]], sep: str) -> Union[List[str], None]:

    __ not lst_of_lst:
        return None

    
    result = []


    for lst in lst_of_lst:
        result.extend(lst)
        result.append(sep)
    
    result.pop()

    return result



    





