
from collections import Counter

___ freq_digit(num: int) -> int:



    return int(Counter(str(num)).most_common(1)[0][0])







