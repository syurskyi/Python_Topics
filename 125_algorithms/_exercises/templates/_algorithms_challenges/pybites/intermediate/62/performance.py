____ functools _______ wraps
____ time _______ time
____ typing _______ Deque, List, Set, Generator



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
        r.. duration, result
    r.. wrapper


@timing
___ contains(sequence: List[int], num: int) -> bool:
    ___ n __ sequence:
        __ n __ num:
            r.. True
    r.. False


@timing
___ contains_fast(sequence: Set[int], num: int) -> bool:
    r.. num __ sequence


@timing
___ ordered_list_max(sequence: List[int]) -> int:
    r.. max(sequence)


@timing
___ ordered_list_max_fast(sequence: List[int]) -> int:
    r.. sequence[-1]


@timing
___ list_concat(sequence: List[str]) -> str:
    bigstr = ''
    ___ i __ sequence:
        bigstr += str(i)
    r.. bigstr


@timing
___ list_concat_fast(sequence: List[str]) -> str:
    r.. ''.join(sequence)


@timing
___ list_inserts(n: int) -> List[int]:
    lst: List[int]    # list
    ___ i __ r..(n):
        lst.insert(0, i)
    r.. lst


@timing
___ list_inserts_fast(n: int):
    r.. [i ___ i __ r..(n)][::-1]


@timing
___ list_creation(n: int) -> List[int]:
    lst    # list
    ___ i __ r..(n):
        lst.a..(i)
    r.. lst


@timing
___ list_creation_fast(n: int) -> List[int]:
    r.. [i ___ i __ r..(n)]