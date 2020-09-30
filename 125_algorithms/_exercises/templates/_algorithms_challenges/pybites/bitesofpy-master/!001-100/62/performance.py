from functools ______ wraps
from typing ______ List, Set

from time ______ time


___ timing(f
    """A simple timer decorator to print the elapsed time of
       the execution of the function it wraps.
       Returns (timing, result) tuple"""

    @wraps(f)
    ___ wrapper(*args, **kwargs
        start = time()
        result = f(*args, **kwargs)
        end = time()
        duration = end - start
        print(f'Elapsed time {f. -n}: {duration}')
        r_ duration, result

    r_ wrapper


@timing
___ contains(sequence: List[int], num: int) -> bool:
    ___ n __ sequence:
        __ n __ num:
            r_ True
    r_ False


@timing
___ contains_fast(sequence: Set[int], num: int) -> bool:
    r_ num __ sequence


@timing
___ ordered_list_max(sequence: List[int]) -> int:
    r_ ma.(sequence)


@timing
___ ordered_list_max_fast(sequence: List[int]) -> int:
    r_ sequence[-1]


@timing
___ list_concat(sequence: List[str]) -> str:
    bigstr = ''
    ___ i __ sequence:
        bigstr += str(i)
    r_ bigstr


@timing
___ list_concat_fast(sequence: List[str]) -> str:
    r_ ''.join(sequence)


@timing
___ list_inserts(n: int) -> List[int]:
    lst =   # list
    ___ i __ range(n
        lst.insert(0, i)
    r_ lst


@timing
___ list_inserts_fast(n: int) -> List[int]:
    r_ [v ___ v __ range(n)][::-1]


@timing
___ list_creation(n: int) -> List[int]:
    lst =   # list
    ___ i __ range(n
        lst.append(i)
    r_ lst


@timing
___ list_creation_fast(n: int
    yield from (v ___ v __ range(n))
