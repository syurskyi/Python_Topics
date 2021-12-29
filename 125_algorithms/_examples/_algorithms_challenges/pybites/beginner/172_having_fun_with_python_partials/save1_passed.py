from functools import partial

def rounding_nums(number, places):
    return round(number, places)


rounder_int = partial(rounding_nums, places=0)
rounder_detailed = partial(rounding_nums, places=4)