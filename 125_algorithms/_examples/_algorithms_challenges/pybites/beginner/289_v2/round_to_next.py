import math
def round_to_next(number: int, multiple: int):



    r = number/multiple


    return math.ceil(r) * multiple

