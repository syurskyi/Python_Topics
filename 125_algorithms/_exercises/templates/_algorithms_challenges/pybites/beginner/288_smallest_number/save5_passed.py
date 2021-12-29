from typing import List
import itertools
import pandas as pd


___ minimum_number(digits):
    try:
        digits = pd.Series(digits).drop_duplicates().tolist()
        list = []
        for i in digits:
            for set in itertools.permutations(digits, r_ N..
                list.append("".join(filter(str.isdigit, str(set))))
        for i in range(len(list)):
            __ list[0] > list[i]:
                list[0] = list[i]
        return int(list[0])
    except:
        return int(0)