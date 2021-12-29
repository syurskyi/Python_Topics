import math

def round_to_next(number: int, multiple: int):
    return math.ceil(number / multiple) * multiple