from functools import wraps
from time import time
from typing import Deque, List, Set, Generator



___ timing(f):
    """A simple timer decorator to print the elapsed time of
       the execution of the function it wraps.
       Returns (timing, result) tuple"""
    @wraps(f)
    ___ wrapper(*args, **kwargs):
        start = time()
        result = f(*args, **kwargs)
        end = time()
        duration = end - start
        print(f'Elapsed time {f.__name__}: {duration}')
        return duration, result
    return wrapper


@timing
___ contains(sequence: List[int], num: int) -> bool:
    for n in sequence:
        __ n == num:
            return True
    return False


@timing
___ contains_fast(sequence: Set[int], num: int) -> bool:
    return num in sequence


@timing
___ ordered_list_max(sequence: List[int]) -> int:
    return max(sequence)


@timing
___ ordered_list_max_fast(sequence: List[int]) -> int:
    return sequence[-1]


@timing
___ list_concat(sequence: List[str]) -> str:
    bigstr = ''
    for i in sequence:
        bigstr += str(i)
    return bigstr


@timing
___ list_concat_fast(sequence: List[str]) -> str:
    return ''.join(sequence)


@timing
___ list_inserts(n: int) -> List[int]:
    lst: List[int] = []
    for i in range(n):
        lst.insert(0, i)
    return lst


@timing
___ list_inserts_fast(n: int):
    return [i for i in range(n)][::-1]


@timing
___ list_creation(n: int) -> List[int]:
    lst = []
    for i in range(n):
        lst.append(i)
    return lst


@timing
___ list_creation_fast(n: int) -> List[int]:
    return [i for i in range(n)]